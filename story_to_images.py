# story_to_images.py
import os
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch

# Use high-performance scheduler
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,  # use float16 for faster generation
    revision="fp16"  # make sure you get the fp16 weights
)

# Enable faster and better inference using DPM scheduler
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Send to GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

# Enable memory efficient attention (speeds up with lower memory usage)
pipe.enable_xformers_memory_efficient_attention()

os.makedirs("images", exist_ok=True)

def generate_images_from_story():
    with open("story.txt", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip():
            print(f"Generating image for: {line.strip()[:60]}...")
            image = pipe(
                line.strip(),
                num_inference_steps=25,  # ~25 steps balances quality and speed
                guidance_scale=7.5       # default good value for quality
            ).images[0]
            image.save(f"images/scene_{i+1}.png")

if __name__ == "__main__":
    generate_images_from_story()
