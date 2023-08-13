 
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
import webbrowser

def download_video(url):
    try:
        # Send a GET request to the YouTube video URL
        response = requests.get(url)

        # Parse the response content with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the video title
        title = soup.find("meta", property="og:title")["content"]

        # Print the video title
        print(f"Video Title: {title}")

        # Create a YouTube object
        yt = YouTube(url)

        # Choose the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Print the video title
        print(f"\nDownloading: {title}")

        # Download the video
        file_path = stream.download(filename=title)

        # Print the completion message
        print("Download completed!")

        # Open the downloaded video
        webbrowser.open(file_path)

    except Exception as e:
        print(f"Error: {str(e)}")

# Prompt the user to input the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Call the download_video function
download_video(video_url)





