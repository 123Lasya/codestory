# story_to_images.py
import requests
import os
import shutil
import re

def clean_sentences(story):
    # Split story into 4 clean, meaningful chunks
    sentences = re.split(r'(?<=[.!?]) +', story)
    chunk_size = max(1, len(sentences) // 4)
    return [' '.join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]

def download_lexica_images(prompt_list):
    os.makedirs("images", exist_ok=True)
    
    for i, prompt in enumerate(prompt_list):
        print(f"Generating image for: {prompt}")
        url = f"https://lexica.art/api/v1/search?q={prompt}"
        response = requests.get(url)

        if response.status_code == 200:
            results = response.json().get("images", [])
            if results:
                image_url = results[0].get("srcSmall")
                img_data = requests.get(image_url, stream=True)
                with open(f"images/image_{i+1}.jpg", "wb") as f:
                    shutil.copyfileobj(img_data.raw, f)
                print(f"Saved images/image_{i+1}.jpg")
            else:
                print(f"No images found for prompt: {prompt}")
        else:
            print("Failed to connect to Lexica API")

if __name__ == "__main__":
    # Read the story
    with open("story.txt", "r") as file:
        story = file.read()
    
    prompts = clean_sentences(story)
    download_lexica_images(prompts)
