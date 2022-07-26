from pytube import Playlist
from sys import argv

link = argv[1]
playlistToDownload = Playlist(link)

print("Currently downloading Audio from Playlist: ", playlistToDownload.title)

for video in playlistToDownload.videos:
    video.streams.get_audio_only().download('./Download/MusicPlaylists')
