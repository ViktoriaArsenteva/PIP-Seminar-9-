from pytube import YouTube

video_link = 'https://www.youtube.com/watch?v=8ZpVwAeLzm4'
yt = YouTube(video_link)
videos = yt.videos
videos.download()