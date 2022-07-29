from pytube import YouTube
from sys import argv

linksList = [
"https://www.youtube.com/watch?v=WmsV3_Z6uYY",
"https://www.youtube.com/watch?v=pLWc6RdrX_E",
"https://www.youtube.com/watch?v=1GT1AsUfntM",
"https://www.youtube.com/watch?v=Q6z9ZguY-UQ",
"https://www.youtube.com/watch?v=9NP_zHE7vO0",
"https://www.youtube.com/watch?v=0Nk5YLz6FLI",
"https://www.youtube.com/watch?v=b_jUdtIfjrI",
"https://www.youtube.com/watch?v=3iZG7azpBr0",
"https://www.youtube.com/watch?v=c-DmtSrhrvM",
"https://www.youtube.com/watch?v=edyXP5pAzu8",
"https://www.youtube.com/watch?v=cBcZz5tv-Cg",
"https://www.youtube.com/watch?v=eQoCkVlk-bQ",
"https://www.youtube.com/watch?v=JZ2blZP6DEE"
]

# link = argv[1]

for x in range(len(linksList)):
    link = linksList[x]
    youtubeObject = YouTube(link)

    print("Currently downloading video of: ", youtubeObject.title)
    print("From: ", youtubeObject.author)
    print("From: ", youtubeObject.length)

    videoFromObject = youtubeObject.streams.get_highest_resolution()

    videoFromObject.download('./Download/Video')
