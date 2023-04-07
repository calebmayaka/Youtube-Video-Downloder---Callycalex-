import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    quality = quality_var.get()
    try:
        video = YouTube(url)
        stream = video.streams.filter(progressive=True, file_extension='mp4', res=quality).first()
        stream.download()
        messagebox.showinfo("YouTube Downloader", f"{video.title} has been downloaded successfully!")
    except Exception as e:
        messagebox.showerror("YouTube Downloader", f"Error downloading {url}: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")

# Create the input frame and widgets
input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=20)

url_label = tk.Label(input_frame, text="Video URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = tk.Entry(input_frame)
url_entry.grid(row=0, column=1, padx=5, pady=5)

quality_label = tk.Label(input_frame, text="Video Quality:")
quality_label.grid(row=1, column=0, padx=5, pady=5)

quality_var = tk.StringVar()
quality_var.set("720p")

quality_menu = tk.OptionMenu(input_frame, quality_var, "144p", "240p", "360p", "480p", "720p", "1080p")
quality_menu.grid(row=1, column=1, padx=5, pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(padx=20, pady=10)

root.mainloop()
