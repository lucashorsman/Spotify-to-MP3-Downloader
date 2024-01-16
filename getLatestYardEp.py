import requests
import re
from pytube import YouTube
import os
import shutil
channel = "https://www.youtube.com/@TheYardPodcast/"
html = requests.get(channel + "/videos").text
info = re.search('(?<={"label":").*?(?="})', html).group()
# url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
url = "https://www.youtube.com/watch?v=MvPYcgjgEN0&"

print(info)
print(url)

yt = YouTube(url)
video = yt.streams.filter(only_audio=True).first()
# check for destination to save file 
print("Enter the destination (leave blank for current directory)") 
destination = str(input(">> ")) or '.'

# download the file 
out_file = video.download(output_path=destination)

# save the file 
base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file)

# move the file to another location
new_location = "D:\\podcast\\The Yard"
shutil.move(new_file, new_location)

# result of success 
print(yt.title + " has been successfully downloaded and moved to " + new_location + ".")





