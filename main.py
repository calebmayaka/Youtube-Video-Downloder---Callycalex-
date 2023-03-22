from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube

# create a window
window = Tk()
window.title("YouTube Downloader")

# create a label and text entry box for the URL
url_label = Label(window, text="Enter the YouTube video URL:")
url_label.pack()
url_entry = Entry(window, width=50)
url_entry.pack()

# function to select the default save location
def select_location():
    # open a file dialog to select the default save location
    default_dir = filedialog.askdirectory()
    # set the text in the location entry box to the selected directory
    location_entry.delete(0, END)
    location_entry.insert(0, default_dir)

# create a label, text entry box, and button for the default save location
location_label = Label(window, text="Select default save location:")
location_label.pack()
location_entry = Entry(window, width=50)
location_entry.pack()
location_button = Button(window, text="Select", command=select_location)
location_button.pack()

# create a label and dropdown menu for the video quality
quality_label = Label(window, text="Select video quality:")
quality_label.pack()
quality_var = StringVar()
quality_var.set("720p")
quality_menu = OptionMenu(window, quality_var, "144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p")
quality_menu.pack()

# function to download a video
def download_video():
    try:
        # create a YouTube object
        video = YouTube(url_entry.get())
        # get the selected quality from the dropdown menu
        quality = quality_var.get()
        # get the stream for the selected quality
        stream = video.streams.filter(file_extension='mp4', res=quality).first()
        # get the default save location from the text entry box
        default_dir = location_entry.get()
        # download the video to the default save location
        stream.download(output_path=default_dir)
        # show a message box when the download is complete
        messagebox.showinfo("YouTube Downloader", f"Download of {video.title} complete!")
    except Exception as e:
        # show a message box if there was an error downloading the video
        messagebox.showerror("YouTube Downloader", f"Error downloading {url_entry.get()}: {str(e)}")

# create a button to download the video
download_button = Button(window, text="Download", command=download_video)
download_button.pack()

# run the window
window.mainloop()
