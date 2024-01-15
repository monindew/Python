import yt_dlp

with yt_dlp.YoutubeDL() as ydl:
    ydl.download(['https://www.youtube.com/watch?v=KwUuUvf1UAs'])

