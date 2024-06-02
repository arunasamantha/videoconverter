#!/usr/bin/env python3

import os
import subprocess
from tkinter import Tk, Label, Button, filedialog, messagebox

def video_to_audio(input_path, output_path):
    try:
        video_to_audio_cmd = f'ffmpeg -i "{input_path}" "{output_path}"'
        subprocess.run(video_to_audio_cmd, shell=True, check=True)
        messagebox.showinfo("Success", f"Successfully converted {os.path.basename(input_path)} to audio!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def browse_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename()
    if input_file_path:
        messagebox.showinfo("File Selected", f"Selected file: {os.path.basename(input_file_path)}")

def save_file_as():
    global output_file_path
    output_file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if output_file_path:
        messagebox.showinfo("Save Location Selected", f"Save location: {os.path.basename(output_file_path)}")

def convert_file():
    if input_file_path and output_file_path:
        video_to_audio(input_file_path, output_file_path)
    else:
        messagebox.showerror("Error", "Please select both the input file and output location before converting.")

def main():
    global input_file_path, output_file_path
    input_file_path = None
    output_file_path = None

    root = Tk()
    root.title("Video to Audio Converter")

    label = Label(root, text="Select a video file to convert to audio")
    label.pack(pady=20)

    browse_button = Button(root, text="Browse Video File", command=browse_file)
    browse_button.pack(pady=10)

    save_button = Button(root, text="Select Save Location", command=save_file_as)
    save_button.pack(pady=10)

    convert_button = Button(root, text="Convert", command=convert_file)
    convert_button.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()
