# from pytube import YouTube

# def download_video(url, resolution, save_path):
#     try:
#         video = YouTube(url)
#         stream = video.streams.filter(res=resolution, progressive=True).first()
        
#         print("جاري تحميل الفيديو...")
#         stream.download(output_path=save_path)
        
#         print("تم التحميل بنجاح!")
#     except Exception as e:
#         print("حدث خطأ أثناء التحميل:", str(e))

# def main():
#     url = input("الرجاء إدخال رابط الفيديو من YouTube: ")
#     resolution = input("الرجاء اختيار الدقة (144, 240, 360, 480, 720, 1080): ")
#     save_path = input("الرجاء إدخال مسار الحفظ: ")
    
#     download_video(url, resolution, save_path)

# if __name__ == "__main__":
#     main()


# #  http://www.youtube.com/watch?v=QuVfXt6j3Ac
#  https://www.youtube.com/watch?v=OUMtKpCUi2I



#*************************************************************************************************


# import requests

# def download_video(url, file_name):
#     response = requests.get(url, stream=True)
#     response.raise_for_status()
    
#     with open(file_name, 'wb') as file:
#         for chunk in response.iter_content(chunk_size=8192):
#             if chunk:
#                 file.write(chunk)

# # Example usage
# video_url = input("Enter the video URL: ")
# file_name = input("Enter the desired file name: ")

# download_video(video_url, file_name)
# print("Video downloaded successfully!")



#----------------------------------------------
# from pytube import YouTube

# def download_video(url):
#     try:
#         # Create a YouTube object
#         yt = YouTube(url)

#         # Get the video title
#         title = yt.title

#         # Print the video title
#         print(f"Downloading: {title}")

#         # Choose the highest resolution stream
#         stream = yt.streams.get_highest_resolution()

#         # Download the video
#         stream.download()

#         # Print the completion message
#         print("Download completed!")

#     except Exception as e:
#         print(f"Error: {str(e)}")

# # Prompt the user to input the YouTube video URL
# video_url = input("Enter the YouTube video URL: ")

# # Call the download_video function
# download_video(video_url)

#---------------------------------------------------------------------






# import requests
# import webbrowser

# def download_video(url, file_name):
#     response = requests.get(url, stream=True)
#     response.raise_for_status()
    
#     with open(file_name, 'wb') as file:
#         for chunk in response.iter_content(chunk_size=8192):
#             if chunk:
#                 file.write(chunk)

# def open_video(video_path):
#     webbrowser.open(video_path)

# # Example usage
# video_url = input("Enter the video URL: ")
# file_name = input("Enter the desired file name with extension (e.g., video.mp4): ")

# download_video(video_url, file_name)
# print("Video downloaded successfully!")

# open_video(file_name)

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





