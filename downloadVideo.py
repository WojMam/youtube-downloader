from pytube import YouTube
from sys import argv

link = argv[1]
youtubeObject = YouTube(link)

print("Currently downloading video of: ", youtubeObject.title)
print("From: ", youtubeObject.author)
print("From: ", youtubeObject.length)

audioFromObject = youtubeObject.streams.get_highest_resolution()

audioFromObject.download('./Download/Video')
