from pytube import YouTube

linksList = [
    "https://www.youtube.com/watch?v=2OOdI2knTjk",
    "https://www.youtube.com/watch?v=2OOdI2knTjk",
]

# link = argv[1]

for x, linksList in enumerate(linksList):
    link = (x, linksList)
    youtubeObject = YouTube(link[x + 1])

    print("Currently downloading video of: ", youtubeObject.title)
    print("From: ", youtubeObject.author)
    print("With length of: ", youtubeObject.length)

    videoFromObject = youtubeObject.streams.get_highest_resolution()

    videoFromObject.download("./Download/Video")
