from pytube import Playlist, YouTube

playlist_url = "https://youtube.com/playlist?list=PLA-It0Cs2sXPlR-yobzqBXqRQxb_2uYL1&si=f60VJdm-JJK1Ci9z"
playlist = Playlist(playlist_url)

print(f"Downloading: {playlist.title}")

for video in playlist.videos:
    print(f"Downloading: {video.title}")
    try:
        stream = video.streams.get_highest_resolution()
        stream.download()
    except Exception as e:
        print(f"Failed to download {video.title}: {e}")
