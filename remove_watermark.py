# remove_watermark.py

import cv2
import numpy as np
import os
from moviepy.video.io.VideoFileClip import VideoFileClip


# === CONFIGURATION ===

input_folder = "videos"
output_folder = "output"

# Make sure folders exist
os.makedirs(output_folder, exist_ok=True)

# === Video paths ===

video_filename = "Join Global March Now.mp4"  # CHANGE this to your video name
video_path = os.path.join(input_folder, video_filename)

temp_video_no_audio_path = os.path.join(output_folder, "temp_no_audio.mp4")
final_output_path = os.path.join(output_folder, "Join_Global_March_Now_no_watermark.mp4")

# === Watermark region (change as needed) ===
# Example: x=10, y=10, width=200, height=60
# Load selected area
with open("selected_area.txt", "r") as f:
    coords = f.read().strip().split(",")
    x, y, w, h = map(int, coords)

print(f"Using area: x={x}, y={y}, w={w}, h={h}")


# === STEP 1: Remove watermark using OpenCV ===

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise Exception(f"Could not open video: {video_path}")

# Video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(temp_video_no_audio_path, fourcc, fps, (width, height))

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Processing {frame_count} frames...")

for i in range(frame_count):
    ret, frame = cap.read()
    if not ret:
        break

    # Inpaint the watermark area
    mask = np.zeros((height, width), np.uint8)
    mask[y:y+h, x:x+w] = 255
    inpainted_frame = cv2.inpaint(frame, mask, 3, cv2.INPAINT_TELEA)

    out.write(inpainted_frame)

    if i % 100 == 0:
        print(f"Frame {i}/{frame_count} processed")

cap.release()
out.release()

print("Video without watermark saved:", temp_video_no_audio_path)

# === STEP 2: Add back original audio ===

print("Adding back original audio...")

video_clip = VideoFileClip(temp_video_no_audio_path)
original_clip = VideoFileClip(video_path)

final_clip = video_clip.with_audio(original_clip.audio)
final_clip.write_videofile(final_output_path, codec='libx264', audio_codec='aac')

print("DONE! Final video saved:", final_output_path)
