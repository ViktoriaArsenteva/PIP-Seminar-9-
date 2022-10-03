from pytube import YouTube
url="https://www.youtube.com/watch?v=n06H7OcPd-g"
video = YouTube(url)
video = video.streams.get_highest_resolution()
video.download()