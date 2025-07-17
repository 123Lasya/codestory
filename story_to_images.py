# story_to_images.py
import os
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

os.makedirs("images", exist_ok=True)

def generate_images_from_story():
    with open("story.txt", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip():
            print(f"Generating image for: {line.strip()[:60]}...")
            image = pipe(line.strip()).images[0]
            image.save(f"images/scene_{i+1}.png")

if __name__ == "__main__":
    generate_images_from_story()
