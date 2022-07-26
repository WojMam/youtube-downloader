from pytube import Playlist
from sys import argv

link = argv[1]
playlistToDownload = Playlist(link)

print("Currently downloading Video from Playlist: ", playlistToDownload.title)

for video in playlistToDownload.videos:
    video.streams.get_highest_resolution().download('./Download/VideoPlaylists')
