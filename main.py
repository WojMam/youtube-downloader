"""This is a main python app module"""

import os
from sys import argv

from pytube import YouTube
import customtkinter as tk


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

        self.iniatiliza_window()

    def iniatiliza_window(self):
        """
        This method is responsible for the initialization of the main window of the app.
        """

        self.window = tk.CTk()
        self.window.title("Youtube Downloader")

        self.window.geometry("400x400")

        self.window.mainloop()


class Utils:
    """
    This is a class that contains all the utility methods for the app.
    """

    def create_results_directory(self):
        """
        This method is checking if the directory for the produced results is available
        in the project and if not- it is creating it in the root of the project.
        """

        if not os.path.exists("Download"):
            os.mkdir("Download")

    def download_video(self, link: str):
        """
        This method is checking if the directory for the produced results is available
        in the project and if not- it is creating it in the root of the project.
        """

        youtube_object = YouTube(link)

        print("Currently downloading video of: ", youtube_object.title)
        print("From: ", youtube_object.author)
        print("With length of: ", youtube_object.length)

        video_from_object = youtube_object.streams.get_highest_resolution()

        video_from_object.download("./Download/Video")

    def download_audio(self, link: str):
        """
        This method is checking if the directory for the produced results is available
        in the project and if not- it is creating it in the root of the project.
        """

        youtube_object = YouTube(link)

        print("Currently downloading audio of: ", youtube_object.title)
        print("From: ", youtube_object.author)
        print("From: ", youtube_object.length)

        audio_from_object = youtube_object.streams.get_audio_only()

        audio_from_object.download("./Download/Music")


if __name__ == "__main__":
    App()
