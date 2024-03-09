""" This module is responsible for the main window class of the app. """

from tkinter import Canvas
import customtkinter as tk

from gui.utils import Utils
from pytube import YouTube
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO


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
        self.tabview = None
        self.button_download_audio = None
        self.button_download_video = None
        self.sidebar_frame = None
        self.logo_label = None
        self.sidebar_button_1 = None
        self.sidebar_button_2 = None
        self.appearance_mode_label = None
        self.appearance_mode_optionemenu = None
        self.scaling_label = None
        self.scaling_optionemenu = None
        self.main_frame = None
        self.iniatiliza_window()

    def iniatiliza_window(self):
        """
        This method is responsible for the initialization of the main window of the app.
        """

        self.window = tk.CTk()
        self.window.title("Youtube Downloader")

        self.window.geometry(f"{1100}x{580}")
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure((2, 3), weight=0)
        self.window.grid_rowconfigure((0, 1, 2), weight=1)

        self.initialize_main_frame()
        self.initialize_sidebar()

        self.window.mainloop()

    def initialize_sidebar(self):
        """
        This method is responsible for the initialization of the sidebar of the app.
        """

        self.sidebar_frame = tk.CTkFrame(self.window, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = tk.CTkLabel(
            self.sidebar_frame,
            text="Welcome to the\nYoutube Downloader!",
            font=tk.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = tk.CTkButton(
            self.sidebar_frame, text="Open results", command=self.sidebar_button_event
        )
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = tk.CTkButton(
            self.sidebar_frame, text="About project", command=self.sidebar_button_event
        )
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = tk.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = tk.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = tk.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = tk.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def initialize_main_frame(self):
        """
        This method is responsible for the initialization of the widgets of the app.
        """

        self.main_frame = tk.CTkFrame(self.window, width=140, corner_radius=0)
        self.main_frame.grid(
            row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )
        self.label = tk.CTkLabel(
            self.main_frame, text="Enter the link of the video you want to download"
        )
        self.label.grid(
            row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

        self.entry = tk.CTkEntry(self.main_frame)
        self.entry.grid(
            row=1, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )
        self.button_load_video = tk.CTkButton(
            self.main_frame,
            text="Load Video",
            command=self.load_video_button_action,
        )
        self.button_load_video.grid(
            row=1, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

        # create tabview
        self.tabview = tk.CTkTabview(self.window, width=250)
        self.tabview.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Video").grid_columnconfigure(1, weight=1)
        self.tabview.add("Audio").grid_columnconfigure(1, weight=1)

        self.button_download_video = tk.CTkButton(
            self.tabview.tab("Video"),
            text="Download Video",
            command=self.download_video_button_action,
        )
        self.button_download_video.grid(
            row=2, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

        self.button_download_audio = tk.CTkButton(
            self.tabview.tab("Audio"),
            text="Download Audio",
            command=self.download_audio_button_action,
        )
        self.button_download_audio.grid(
            row=2, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

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

    def load_video_button_action(self):
        """
        This method is responsible for the action of the download audio button.
        """
        ui_element = self.main_frame
        link = self.entry.get()
        self.load_video_preview(ui_element, link)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        Utils.change_appearance_mode_event(self, new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        Utils.change_scaling_event(self, new_scaling)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def load_video_preview(self, ui_element, link):
        # link = self.entry.get()  # imageurl
        # video = YouTube(link)
        thumbnail_url = YouTube(link).thumbnail_url.replace(
            "hq720.jpg", "maxresdefault.jpg"
        )
        # thumbnail_url = video.thumbnail_url
        print(thumbnail_url)
        urllib.request.urlretrieve(thumbnail_url, "local-filename.jpg")

        video_preview = Image.open("local-filename.jpg")
        resized_video_preview = video_preview.resize((400, 250))
        video_preview_widget = tk.CTkImage(
            dark_image=resized_video_preview,
            light_image=resized_video_preview,
            size=(400, 250),
        )
        video_preview_widget.configure()
        self.video_preview_label = tk.CTkLabel(
            ui_element,
            text="",
            image=video_preview_widget,
            anchor="w",
        )
        self.video_preview_label.grid(
            row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20)
        )
