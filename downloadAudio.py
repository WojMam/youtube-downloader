from pytube import YouTube
from sys import argv

link = argv[1]
youtubeObject = YouTube(link)

print("Currently downloading audio of: ", youtubeObject.title)
print("From: ", youtubeObject.author)
print("From: ", youtubeObject.length)

audioFromObject = youtubeObject.streams.get_audio_only()

audioFromObject.download('./Download/Music')
