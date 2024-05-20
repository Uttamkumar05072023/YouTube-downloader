from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube


# Functioning Part
def main(n):
    link = entryLabel.get()
    if link != "":
        try:
            data = YouTube(link)
            match n:
                case 1:
                    highQualityVideo = data.streams.get_highest_resolution()
                    path = filedialog.asksaveasfilename(defaultextension="mp4")
                case 2:
                    lowQualityVideo = data.streams.get_lowest_resolution()
                    path = filedialog.asksaveasfilename(defaultextension="mp4")
                case 3:
                    audio = data.streams.get_audio_only()
                    path = filedialog.asksaveasfilename(defaultextension="mp3")
            if path != "":
                l = path.split("/")
                name = l.pop()
                new_path = "/".join(l)
            match n:
                case 1:
                    highQualityVideo.download(output_path=new_path, filename=name)
                    messagebox.showinfo("Done", "Video file downloaded successfully...")
                case 2:
                    lowQualityVideo.download(output_path=new_path, filename=name)
                    messagebox.showinfo("Done", "Video file downloaded successfully...")
                case 3:
                    audio.download(output_path=new_path, filename=name)
                    messagebox.showinfo("Done", "Audio file downloaded successfully...")
        except:
            messagebox.showerror("Error", "Something went wrong!!!")


def high_720():
    main(1)


def low_360():
    main(2)


def audio():
    main(3)


# GUI Part
root = Tk()
root.title("Youtube audio/video downloader")
root.iconbitmap("icon.ico")
root.resizable(False, False)
root.geometry("400x500")
root.configure(background="plum1")

mainLabel = Label(root, text="YouTube audio/video downloader", font=("Comic Sans MS", 18, "bold"),
                  background="OliveDrab2", foreground="purple", height=2)
mainLabel.pack(fill=X)

urlLabel = Label(root, text="Enter/Past the URL", font=("Comic Sans MS", 14, "bold"), background="plum1")
urlLabel.pack(pady=15, ipady=5, ipadx=18)
entryLabel = Entry(root, font=("arial", 13), width=40, foreground="blue")
entryLabel.pack(ipady=7, ipadx=1)

videoButtonFrame = LabelFrame(root, background="plum1", borderwidth=0)
videoButtonFrame.pack(pady=20)
videoLabel = Label(videoButtonFrame, text="Download video", font=("Comic Sans MS", 14, "bold"))
videoLabel.grid(row=0, column=0, columnspan=2, pady=20, ipady=5, ipadx=18)

highButton = Button(videoButtonFrame, text="720p", font=("Comic Sans MS", 14, "bold"), foreground="blue",
                    activebackground="OliveDrab2", activeforeground="blue", command=high_720)
highButton.grid(row=1, column=0, padx=30, ipadx=10)

lowButton = Button(videoButtonFrame, text="360p", font=("Comic Sans MS", 14, "bold"), foreground="blue",
                   activebackground="OliveDrab2", activeforeground="blue", command=low_360)
lowButton.grid(row=1, column=1, padx=30, ipadx=10)

audioButtonLabel = Label(root, text="Download audio", font=("Comic Sans MS", 14, "bold"))
audioButtonLabel.pack(pady=20, ipady=5, ipadx=18)

audioButton = Button(root, text="mp3", font=("Comic Sans MS", 14, "bold"), foreground="blue",
                     activebackground="OliveDrab2", activeforeground="blue", command=audio)
audioButton.pack(padx=10, ipadx=10)

root.mainloop()
