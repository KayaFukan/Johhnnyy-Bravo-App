<<<<<<< HEAD
import tkinter as tk
from tkinter import filedialog
import yt_dlp

class YouTubeDownloader(tk.Toplevel):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.title("YouTube Media Downloader")
        self.geometry("400x250")
        self.center_window()
        self.create_widgets()

    def center_window(self):
        self.overrideredirect(True)
        window_width = 400
        window_height = 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        self.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

    def create_widgets(self):
        label_url = tk.Label(self, text="URL:")
        label_url.pack(pady=5)

        self.entry_url = tk.Entry(self, width=50)
        self.entry_url.pack(pady=5)

        self.video_var = tk.BooleanVar(value=True)

        frame = tk.Frame(self)
        frame.pack()

        radio_audio = tk.Radiobutton(frame, text="Audio", variable=self.video_var, value=False)
        radio_audio.grid(row=0, column=0, padx=10)

        radio_video = tk.Radiobutton(frame, text="Video", variable=self.video_var, value=True)
        radio_video.grid(row=0, column=1, padx=10)

        download_button = tk.Button(self, text="Download", command=self.download_media)
        download_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack(pady=10)

        exit_button = tk.Button(self, text="EXIT", command=self.exit_converter)
        exit_button.pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def download_media(self):
        youtube_url = self.entry_url.get()
        output_dir = filedialog.askdirectory(title="Select Download Directory")

        if output_dir:
            is_video = self.video_var.get()
            if youtube_url:
                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' if is_video else 'bestaudio[ext=webm]/bestaudio',
                    'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
                }

                if not is_video:
                    ydl_opts['postprocessors'] = [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]

                try:
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([youtube_url])
                    self.show_message("Download Successful!")
                except Exception as e:
                    self.show_message(f"Error: {str(e)}", color="red")

    def show_message(self, message, color="green"):
        self.result_label.config(text=message, fg=color)
        self.result_label.after(3000, self.clear_message)

    def clear_message(self):
        self.result_label.config(text="", fg="black")

    def go_back(self):
        self.destroy()
        self.main_app.show_main_window()

    def exit_converter(self):
        self.quit()
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = YouTubeDownloader(root)
    app.mainloop()
=======
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

class YouTubeDownloader(tk.Tk):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app  # Ana uygulama referansı
        self.title("YouTube Media Downloader")
        self.geometry("400x250")
        self.center_window()  # Ekranı ortala
        self.create_widgets()

    def center_window(self):
        window_width = 400
        window_height = 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        self.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

    def create_widgets(self):
        self.overrideredirect(True)
        label_url = tk.Label(self, text="URL:")
        label_url.pack(pady=5)

        self.entry_url = tk.Entry(self, width=50)
        self.entry_url.pack(pady=5)

        self.video_var = tk.BooleanVar()
        self.video_var.set(False)

        frame = tk.Frame(self)
        frame.pack()

        radio_audio = tk.Radiobutton(frame, text="Audio", variable=self.video_var, value=False)
        radio_audio.grid(row=0, column=0, padx=10)

        radio_video = tk.Radiobutton(frame, text="Video", variable=self.video_var, value=True)
        radio_video.grid(row=0, column=1, padx=10)

        download_button = tk.Button(self, text="Download", command=self.download_media)
        download_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack(pady=10)

        exit_button = tk.Button(self, text="EXIT", command=self.exit_converter)
        exit_button.pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def download_media(self):
        youtube_url = self.entry_url.get()
        output_dir = filedialog.askdirectory(title="Select Download Directory")

        if output_dir:
            is_video = self.video_var.get()
            if youtube_url:
                yt = YouTube(youtube_url)
                if is_video:
                    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                    output_file_name = f"{output_dir}/downloaded_video.mp4"
                else:
                    stream = yt.streams.filter(only_audio=True).first()
                    output_file_name = f"{output_dir}/downloaded_audio.mp3"
                
                stream.download(output_path=output_dir, filename=output_file_name)
                self.show_message("Download Successful!")

    def show_message(self, message, color="green"):
        self.result_label.config(text=message, fg=color)
        self.result_label.after(3000, self.clear_message)

    def clear_message(self):
        self.result_label.config(text="", fg="black")

    def go_back(self):
        self.destroy()
        self.main_app.show_main_window()  # Ana uygulama penceresini göster

    def exit_converter(self):
        self.quit()
        self.destroy()
>>>>>>> 16064d83bed140367f474fd73f0bd83b098ef722
