"""This is a main python app module"""

import os
from sys import argv

from pytube import YouTube


def create_results_directory():
    """
    This method is checking if the directory for the produced results is available
    in the project and if not- it is creating it in the root of the project.
    """

    if not os.path.exists("Download"):
        os.mkdir("Download")


def download_video():
    """
    This method is checking if the directory for the produced results is available
    in the project and if not- it is creating it in the root of the project.
    """

    links_list = [
        "https://www.youtube.com/watch?v=2OOdI2knTjk",
        "https://www.youtube.com/watch?v=2OOdI2knTjk",
    ]

    for x, links_list in enumerate(links_list):
        link = (x, links_list)
        youtube_object = YouTube(link[x + 1])

        print("Currently downloading video of: ", youtube_object.title)
        print("From: ", youtube_object.author)
        print("With length of: ", youtube_object.length)

        video_from_object = youtube_object.streams.get_highest_resolution()

        video_from_object.download("./Download/Video")


def download_audio():
    """
    This method is checking if the directory for the produced results is available
    in the project and if not- it is creating it in the root of the project.
    """

    link = argv[1]
    youtube_object = YouTube(link)

    print("Currently downloading audio of: ", youtube_object.title)
    print("From: ", youtube_object.author)
    print("From: ", youtube_object.length)

    audio_from_object = youtube_object.streams.get_audio_only()

    audio_from_object.download("./Download/Music")


if __name__ == "__main__":
    download_video()
