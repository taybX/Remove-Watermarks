Remove Watermark from Video

This project provides a Python tool to remove a watermark or logo from a video by inpainting the selected region and preserving the original audio.

---

Features

- Select the watermark area interactively using a simple GUI
- Remove watermark by inpainting that region frame-by-frame
- Preserve the original audio track in the final output video
- Compatible with MoviePy v2.0.0 and above
- Works on Windows, Linux, and Mac

---

Requirements

- Python 3.10+
- OpenCV
- MoviePy (installed from GitHub tag v2.0.0)
- NumPy

Install dependencies using:

pip install -r requirements.txt

---

Usage

Step 1: Select watermark area

Run the GUI script to select the area containing the watermark/logo:

python select_area.py

- A window will open showing a frame from the video
- Drag with the mouse to select the watermark region
- Coordinates will be saved automatically to selected_area.txt

Step 2: Remove watermark

Run the main script to remove the watermark and save the output:

python remove_watermark.py

- The script will read selected_area.txt for coordinates
- It will process the video frames and remove the watermark
- The output video with audio will be saved in the output folder

---

Project Structure

/PythonProjecttest
├── videos/                # Place your input videos here
├── output/                # Processed videos will be saved here
├── remove_watermark.py    # Main watermark removal script
├── select_area.py         # GUI to select watermark area
├── selected_area.txt      # Stores selected watermark coordinates
├── requirements.txt       # Python dependencies
└── .venv                  # Python virtual environment (optional)

---

Notes

- Make sure your video file is placed inside the videos folder
- You can change the video filename inside the scripts if needed
- The project uses MoviePy v2.0.0 (installed from GitHub) due to API changes

---

License

This project is open source and free to use.

---

Contact

For any questions or help, feel free to open an issue on GitHub or contact the author.

---

Enjoy watermark-free videos! 🎉🚀
