# downloader.py
import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]',
        'outtmpl': '%(title)s_video.%(ext)s',
        'postprocessors': [],
        'merge_output_format': None,
        'noplaylist': True,
        'overwrites': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': '%(title)s_audio.%(ext)s',
        'postprocessors': [],
        'merge_output_format': None,
        'noplaylist': True,
        'overwrites': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
