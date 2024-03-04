""" This module contains the utility methods for the app. """

import os

from pytube import YouTube


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
