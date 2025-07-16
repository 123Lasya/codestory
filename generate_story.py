import os
import google.generativeai as genai

# Replace with your Gemini API key
GOOGLE_API_KEY = "AIzaSyBkhtG0SRZNknrHZW8N0K6MlNx3sqmGiOY"  # 👈 Replace this
genai.configure(api_key=GOOGLE_API_KEY)

def generate_story(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")

    story_prompt = f"Explain {prompt} as a story for kids in a friendly tone with scenes separated clearly. Use simple language and add a fun, adventurous feel and avoide using copyrighted or trademarked content and don’t violate the terms of the Stable Diffusion model licenses while generating the story"
    response = model.generate_content(story_prompt)
    story = response.text

    with open("story.txt", "w") as f:
        f.write(story)

    return story

if __name__ == "__main__":
    topic = input("Enter coding topic: ")
    print(generate_story(topic))
