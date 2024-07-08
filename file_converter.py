import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pdf2image import convert_from_path

class FileConverter(tk.Tk):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app  # Ana uygulama referansı
        self.title("File Converter")
        self.geometry("400x400")
        self.center_window()  # Ekranı ortala
        self.create_widgets()

    def center_window(self):
        window_width = 400
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        self.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

    def create_widgets(self):
        self.overrideredirect(True)
        label = tk.Label(self, text="Select a conversion type:")
        label.pack(pady=20)

        # Video Conversion
        video_frame = tk.Frame(self, bd=1, relief="solid", padx=10, pady=10)
        video_frame.pack(pady=10, fill="x")

        #video_label = tk.Label(video_frame, text="Video Conversion:")
        #video_label.pack()

        video_buttons_frame = tk.Frame(video_frame)  # Frame for video conversion buttons
        video_buttons_frame.pack(pady=10)

        mp4_to_avi_button = tk.Button(video_buttons_frame, text="MP4 to AVI", command=self.convert_mp4_to_avi)
        mp4_to_avi_button.pack(side="left", padx=5)

        avi_to_mp4_button = tk.Button(video_buttons_frame, text="AVI to MP4", command=self.convert_avi_to_mp4)
        avi_to_mp4_button.pack(side="left", padx=5)

        mkv_to_mp4_button = tk.Button(video_buttons_frame, text="MKV to MP4", command=self.convert_mkv_to_mp4)
        mkv_to_mp4_button.pack(side="left", padx=5)

        mp4_to_mkv_button = tk.Button(video_buttons_frame, text="MP4 to MKV", command=self.convert_mp4_to_mkv)
        mp4_to_mkv_button.pack(side="left", padx=5)

        # Audio Conversion
        audio_frame = tk.Frame(self, bd=1, relief="solid", padx=10, pady=10)
        audio_frame.pack(pady=10, fill="x")

        audio_label = tk.Label(audio_frame, text="Audio Conversion:")
        audio_label.pack()

        audio_buttons_frame = tk.Frame(audio_frame)  # Frame for audio conversion buttons
        audio_buttons_frame.pack(pady=10)

        wav_to_mp3_button = tk.Button(audio_buttons_frame, text="WAV to MP3", command=self.convert_wav_to_mp3)
        wav_to_mp3_button.pack(side="left", padx=5)

        mp3_to_wav_button = tk.Button(audio_buttons_frame, text="MP3 to WAV", command=self.convert_mp3_to_wav)
        mp3_to_wav_button.pack(side="left", padx=5)

        m4a_to_mp3_button = tk.Button(audio_buttons_frame, text='M4A to MP3', command=self.convert_m4a_to_mp3)
        m4a_to_mp3_button.pack(side='left', padx=5)

        mp3_to_m4a_button = tk.Button(audio_buttons_frame, text='MP3 to M4A', command=self.convert_mp3_to_m4a)
        mp3_to_m4a_button.pack(side='left', padx=5)

        # Video to mp3 Conversion
        video_to_audio_frame = tk.Frame(self, bd=1, relief="solid", padx=10, pady=10)
        video_to_audio_frame.pack(pady=10, fill="x")

        video_to_audio_label = tk.Label(video_to_audio_frame, text="Video to Audio Conversion:")
        video_to_audio_label.pack()

        video_to_audio_buttons_frame = tk.Frame(video_to_audio_frame)  # Frame for pdf conversion buttons
        video_to_audio_buttons_frame.pack(pady=10)

        video_to_audio_button = tk.Button(video_to_audio_buttons_frame, text="Video to Audio", command=self.convert_video_to_audio)
        video_to_audio_button.pack(side="left", padx=5)

        # Back Button
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack(pady=10)

        # Exit Button
        exit_button = tk.Button(self, text="EXIT", command=self.exit_converter)
        exit_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()


    def convert_mp4_to_avi(self):
        input_file = filedialog.askopenfilename(title="Select MP4 File", filetypes=[("MP4 Files", "*.mp4")])
        output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".avi", filetypes=[("AVI Files", "*.avi")])
        if input_file and output_file:
            video_clip = VideoFileClip(input_file)
            video_clip.write_videofile(output_file)
            self.show_message("MP4 to AVI Conversion Successful!")

    def convert_avi_to_mp4(self):
        input_file = filedialog.askopenfilename(title="Select AVI File", filetypes=[("AVI Files", "*.avi")])
        output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".mp4", filetypes=[("MP4 Files", "*.mp4")])
        if input_file and output_file:
            video_clip = VideoFileClip(input_file)
            video_clip.write_videofile(output_file)
            self.show_message("AVI to MP4 Conversion Successful!")
    
    def convert_mkv_to_mp4(self):
        input_file = filedialog.askopenfilename(title="Select MKV File", filetypes=[("MKV Files", "*.mkv")])
        output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".mp4", filetypes=[("MP4 Files", "*.mp4")])
        if input_file and output_file:
            video_clip = VideoFileClip(input_file)
            video_clip.write_videofile(output_file)
            self.show_message("MKV to MP4 Conversion Successful!")

    def convert_mp4_to_mkv(self):
        input_file = filedialog.askopenfilename(title="Select MP4 File", filetypes=[("MP4 Files", "*.mp4")])
        output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".mkv", filetypes=[("MKV Files", "*.mkv")])
        if input_file and output_file:
            video_clip = VideoFileClip(input_file)
            video_clip.write_videofile(output_file)
            self.show_message("MP4 to MKV Conversion Successful!")

    def convert_wav_to_mp3(self):
        input_file = filedialog.askopenfilename(title="Select WAV File", filetypes=[("WAV Files", "*.wav")])
        output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
        if input_file and output_file:
            audio = AudioSegment.from_wav(input_file)
            audio.export(output_file, format="mp3")
            self.show_message("WAV to MP3 Conversion Successful!")

    def convert_mp3_to_wav(self):
        input_file = filedialog.askopenfilename(title="Select MP3 File", filetypes=[("MP3 Files", "*.mp3")])
        output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".wav", filetypes=[("WAV Files", "*.wav")])
        if input_file and output_file:
            audio = AudioSegment.from_mp3(input_file)
            audio.export(output_file, format="wav")
            self.show_message("MP3 to WAV Conversion Successful!")

    def convert_m4a_to_mp3(self):
        input_file = filedialog.askopenfilename(title="Select M4A File", filetypes=[("M4A Files", "*.m4a")])
        output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
        if input_file and output_file:
            audio = AudioSegment.from_file(input_file, format="m4a")
            audio.export(output_file, format="mp3")
            self.show_message("M4A to MP3 Conversion Successful!")
    
    def convert_mp3_to_m4a(self):
        input_file = filedialog.askopenfilename(title="Select MP3 File", filetypes=[("MP3 Files", "*.mp3")])
        output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".m4a", filetypes=[("M4A Files", "*.m4a")])
        if input_file and output_file:
            audio = AudioSegment.from_file(input_file, format="mp3")
            audio.export(output_file, format="m4a")
            self.show_message("MP3 to M4A Conversion Successful!")

    def convert_video_to_audio(self):
        input_file = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
        if input_file and output_file:
            video_clip = VideoFileClip(input_file)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(output_file)
            self.show_message("Video to Audio Conversion Successful!")

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

# Ana Uygulama
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Media Converter")
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
        label = tk.Label(self, text="Select an option:")
        label.pack(pady=20)

        youtube_button = tk.Button(self, text="YouTube Downloader", command=self.open_youtube_downloader)
        youtube_button.pack(pady=10)

        file_converter_button = tk.Button(self, text="File Converter", command=self.open_file_converter)
        file_converter_button.pack(pady=10)

    def open_youtube_downloader(self):
        self.withdraw()  # Ana pencereyi gizle
        youtube_app = YouTubeDownloader(self)  # Ana pencereyi parametre olarak geçir
        youtube_app.protocol("WM_DELETE_WINDOW", self.show_main_window)  # Kapatma tuşuna basıldığında ana pencereyi göster
        youtube_app.mainloop()

    def open_file_converter(self):
        self.withdraw()  # Ana pencereyi gizle
        file_converter_app = FileConverter(self)  # Ana pencereyi parametre olarak geçir
        file_converter_app.protocol("WM_DELETE_WINDOW", self.show_main_window)  # Kapatma tuşuna basıldığında ana pencereyi göster
        file_converter_app.mainloop()

    def show_main_window(self):
        self.deiconify()  # Ana pencereyi tekrar göster

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
