import yt_dlp

playlist_url = "https://youtu.be/kBKA3g8WTuE?si=HTjjO1kTyxMSJ_6v"
ydl_opts = {
    'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s',
    'format': 'best',
    'noplaylist': False,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
