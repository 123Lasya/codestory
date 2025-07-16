from moviepy import *
import os
def create_video_with_subtitles():
    image_folder = "images"
    audio_path = "audio/story.mp3"
    output_path = "video/final_with_subtitles.mp4"

    os.makedirs("video", exist_ok=True)

    image_files = sorted(
        [os.path.join(image_folder, img) for img in os.listdir(image_folder)],
        key=lambda x: int(x.split('_')[-1].split('.')[0])
    )

    with open("story.txt", "r") as f:
        subtitles = [line.strip() for line in f.readlines() if line.strip()]

    clips = []
    for i, image_path in enumerate(image_files):
        img_clip = ImageClip(image_path).set_duration(3)

        if i < len(subtitles):
            txt = TextClip(subtitles[i], fontsize=30, color='white', bg_color='black')
            txt = txt.set_position(('center', 'bottom')).set_duration(3)
            img_clip = CompositeVideoClip([img_clip, txt])

        clips.append(img_clip)

    final = concatenate_videoclips(clips, method="compose")
    final = final.set_audio(AudioFileClip(audio_path))
    final.write_videofile(output_path, fps=24)
