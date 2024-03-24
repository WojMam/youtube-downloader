""" This module contains the utility methods for the app. """

import os
import logging
import platform
import subprocess

from pytube import YouTube
import customtkinter as tk


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

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """
        This method is responsible for the event of changing the appearance mode of the app.
        """

        tk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        """
        This method is responsible for the event of changing the scaling of the app.
        """

        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        tk.set_widget_scaling(new_scaling_float)

    def open_results_dir(self):
        """
        This method opens results directory in system explorer.
        """

        path = "../results"
        if platform.system() == "Windows":
            path = os.path.join(os.path.dirname(__file__), "../Download")
            # Line below has to be disabled in pylint due to the lack of this method in Unix os
            # which the pylint is ran on.
            os.startfile(path)  # pylint: disable=no-member
            logging.info("The results directory has been opened (windows)")
        elif platform.system() == "Darwin":
            with subprocess.Popen(["open", path]) as sub:
                logging.info(
                    "The results directory has been opened (linux): %s", sub.returncode
                )
        else:
            with subprocess.Popen(["xdg-open", path]) as sub:
                logging.info(
                    "The results directory has been opened (macOS): %s", sub.returncode
                )
