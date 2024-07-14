<<<<<<< HEAD
import tkinter as tk
from youtube_downloader import YouTubeDownloader
from file_converter import FileConverter

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Media Converter")
        self.geometry("400x250")
        self.center_window()
        self.create_widgets()
   
    def center_window(self):
        self.overrideredirect(True)
        window_width = 400
        window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        self.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")
   
    def create_widgets(self):
        label = tk.Label(self, text="Welcome to Johhnny Bravo App", font=('Arial',14), fg='Orange')
        label.pack(pady=10)
        
        youtube_button = tk.Button(self, text="YouTube Downloader", command=self.open_youtube_downloader)
        youtube_button.pack(pady=10)

        file_converter_button = tk.Button(self, text="File Converter", command=self.open_file_converter)
        file_converter_button.pack(pady=10)

        exit_button = tk.Button(self, text="EXIT", command=self.exit_converter)
        exit_button.pack(pady=10)

    def open_youtube_downloader(self):
        self.withdraw()
        youtube_app = YouTubeDownloader(self)
        youtube_app.protocol("WM_DELETE_WINDOW", self.show_main_window)
        youtube_app.mainloop()

    def open_file_converter(self):
        self.withdraw()
        file_converter_app = FileConverter(self)
        file_converter_app.protocol("WM_DELETE_WINDOW", self.show_main_window)
        file_converter_app.mainloop()

    def show_main_window(self):
        self.deiconify()
   
    def exit_converter(self):
        self.quit()
        self.destroy()
       
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
=======
import tkinter as tk
from youtube_downloader import YouTubeDownloader
from file_converter import FileConverter

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Media Converter")
        self.geometry("400x250")
        self.center_window()
        self.create_widgets()
    
    def center_window(self):
        window_width = 400
        window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        self.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")
    
    

    def create_widgets(self):
        self.overrideredirect(True)
        label = tk.Label(self, text="Welcome to Johhnny Bravo App", font=('Arial',14),fg='Orange')
        label.pack(pady=10)
        #label = tk.Label(self, text="Select an option:")
        #label.pack(pady=20)

        youtube_button = tk.Button(self, text="YouTube Downloader", command=self.open_youtube_downloader)
        youtube_button.pack(pady=10)

        file_converter_button = tk.Button(self, text="File Converter", command=self.open_file_converter)
        file_converter_button.pack(pady=10)

        exit_button = tk.Button(self, text="EXIT", command=self.exit_converter)
        exit_button.pack(pady=10)

    def open_youtube_downloader(self):
        self.withdraw()
        youtube_app = YouTubeDownloader(self)
        youtube_app.protocol("WM_DELETE_WINDOW", self.show_main_window)
        youtube_app.mainloop()

    def open_file_converter(self):
        self.withdraw()
        file_converter_app = FileConverter(self)
        file_converter_app.protocol("WM_DELETE_WINDOW", self.show_main_window)
        file_converter_app.mainloop()

    def show_main_window(self):
        self.deiconify()  # Ana pencereyi tekrar göster
    
    def exit_converter(self):
        self.quit()
        self.destroy()
        
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
>>>>>>> 16064d83bed140367f474fd73f0bd83b098ef722
