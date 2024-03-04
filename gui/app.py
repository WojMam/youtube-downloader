""" This module is responsible for the main window class of the app. """

import customtkinter as tk

from gui.utils import Utils


class App:
    """
    This is the main class of the app. It is responsible for the user interaction
    and the control of the app.
    """

    def __init__(self):
        """
        This is the main class of the app. It is responsible for the user interaction
        and the control of the app.
        """
        self.label = None
        self.entry = None
        self.button = None
        self.button_download_audio = None
        self.button_download_video = None
        self.iniatiliza_window()

    def iniatiliza_window(self):
        """
        This method is responsible for the initialization of the main window of the app.
        """

        self.window = tk.CTk()
        self.window.title("Youtube Downloader")

        self.window.geometry("400x400")

        self.initialize_widgets()

        self.window.mainloop()

    def initialize_widgets(self):
        """
        This method is responsible for the initialization of the widgets of the app.
        """

        self.label = tk.CTkLabel(
            self.window, text="Enter the link of the video you want to download"
        )
        self.label.pack()

        self.entry = tk.CTkEntry(self.window)
        self.entry.pack()

        self.button_download_video = tk.CTkButton(
            self.window,
            text="Download Video",
            command=self.download_video_button_action,
        )
        self.button_download_video.pack()

        self.button_download_audio = tk.CTkButton(
            self.window,
            text="Download Audio",
            command=self.download_audio_button_action,
        )
        self.button_download_audio.pack()

    def download_video_button_action(self):
        """
        This method is responsible for the action of the download video button.
        """

        link = self.entry.get()

        Utils.download_video(self, link)

    def download_audio_button_action(self):
        """
        This method is responsible for the action of the download audio button.
        """

        link = self.entry.get()

        Utils.download_audio(self, link)
