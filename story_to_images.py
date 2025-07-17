# story_to_images.py
import os
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

# Load model with FP16 for speed (if GPU supports it)
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    revision="fp16"
)

# Use an efficient scheduler
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Enable xFormers for faster generation if available
pipe.enable_xformers_memory_efficient_attention()

# Move pipeline to GPU or CPU based on availability
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

# Ensure images folder exists
os.makedirs("images", exist_ok=True)

def generate_images_from_story():
    with open("story.txt", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        prompt = line.strip()
        if prompt:
            print(f"Generating image for: {prompt[:60]}...")
            image = pipe(
                prompt,
                num_inference_steps=20,  # Fewer steps = faster generation (~15-30 sec/image)
                guidance_scale=7.5       # Controls prompt adherence
            ).images[0]
            image.save(f"images/scene_{i+1}.png")

if __name__ == "__main__":
    generate_images_from_story()
