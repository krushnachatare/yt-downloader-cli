import os
import yt_dlp
from pathlib import Path


os.system("title YT Downloader")
os.system("color 0F")  # Black background, bright white text
os.system("cls")

banner = r"""
██╗   ██╗████████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗
╚██╗ ██╔╝╚══██╔══╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ╚████╔╝    ██║       ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
  ╚██╔╝     ██║       ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
   ██║      ██║       ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
   ╚═╝      ╚═╝       ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""


RESET = "\033[0m"

for line in banner.splitlines():
    print((line + RESET).center(120))

print()
print("=" * 120)
print("Fast • Secure • Open Source • Powered by yt-dlp".center(120))
print("=" * 120)



print("\nNOTE: Video quality is already set to highest available.")
url = input("\nEnter the URL of Youtube video: ")

downloads = Path.home() / "Downloads"

print("\nIn Which format do you want to download the video:\n1. mp3\n2. mp4")
output_format = input("\nEnter your choice(1 or 2):")




if output_format == "2":

    vid_settings = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": str(downloads / "%(title)s.%(ext)s"),
        "quite": False,
        "noplaylist": True
    }
    print("Starting download...")
    try:
        with yt_dlp.YoutubeDL(vid_settings) as ydl:
            ydl.download([url])
        print("Done..!")
    except Exception as e:
        print("\n--- ERROR DETAILS ---")
        print(repr(e))

elif output_format == "1":
    
    audio_settings = {
        'format': 'bestaudio/best',
        "noplaylist": True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
            }],
        'outtmpl': str(downloads / "%(title)s.%(ext)s"),
    }

    print("Starting download...")
    try:
        with yt_dlp.YoutubeDL(audio_settings) as ydl:
            ydl.download([url])
        print("Done..!")
    except Exception as e:
        print("\n--- ERROR DETAILS ---")
        print(repr(e))

else:    
    print("Invalid output format!")
    

