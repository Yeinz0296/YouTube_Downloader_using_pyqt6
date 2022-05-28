from pytube import YouTube
import os

link = 'https://youtu.be/qOXDoYUgNlU'
yt = YouTube(link)
path = 'download'

#Title of video
print("Title: ", yt.title)
#Number of views of video
print("Number of views: ", yt.views)
#Length of the video
print("Length of video: ", yt.length, "seconds")
#Description of video
#print("Description: ", yt.description)
#Rating
#print("Ratings: ", yt.rating)
#print(yt.streams.filter(file_extension='mp4'))

#yd = yt.streams.filter(res='144p')
ys = yt.streams.get_by_itag(22)

ys.download(path)

