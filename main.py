import os
from pytube import Playlist

# Define the YouTube playlist link
playlist_link = str(input("Enter the YouTube playlist link: "))

# Specify the download path
download_path = os.path.dirname(os.path.abspath(__file__))

# Function to download videos in 480p
def download_videos(playlist_link, download_path):
    playlist = Playlist(playlist_link)

    for video in playlist.videos:
        try:
            # Try to get 480p resolution
            video_stream_480p = video.streams.filter(res="480p").first()

            if video_stream_480p:
                print(f"Downloading {video.title} in 480p...")
                video_stream_480p.download(download_path)
                print(f"{video.title} downloaded successfully in 480p.")
            else:
                # If 480p is not available, try 720p
                video_stream_720p = video.streams.filter(res="720p").first()

                if video_stream_720p:
                    print(f"Downloading {video.title} in 720p...")
                    video_stream_720p.download(download_path)
                    print(f"{video.title} downloaded successfully in 720p.")
                else:
                    print(f"No 480p or 720p resolution available for {video.title}. Skipping.")
        except Exception as e:
            print(f"Error downloading {video.title}: {str(e)}")

if __name__ == "__main__":
    download_videos(playlist_link, download_path)
