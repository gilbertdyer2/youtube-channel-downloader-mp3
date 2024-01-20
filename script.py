import scrapetube
from pytube import YouTube
import os
import re


# -------------- PARAMETERS -------------- #
# CHANNEL_URL: Channel URL, copied directly from channel home page
# DOWNLOAD_LIMIT_IN_MEGABYTES: Add buffer if necessary: Current implementation will stop slightly over the limit.
# MAX_DOWNLOADS = Max number of videos to download. Setting to -1 downloads all videos on a channel.
# OUTPUT_FOLDER: Directory to add files
CHANNEL_URL = 'https://www.youtube.com/channel/UC33iUQUpJTkIy4WPCkK_mLA' 
DOWNLOAD_LIMIT_IN_MEGABYTES = 100
MAX_DOWNLOADS = -1             
OUTPUT_FOLDER = r'test-samples'                              
# ---------------------------------------- #                             

def downloadvideo(videoId):
    yt = YouTube('http://youtube.com/watch?v=' + videoId)
    video = yt.streams.filter(only_audio=True).first()
    
   
    videofile = video.download(output_path=OUTPUT_FOLDER, 
                               filename = f"{yt.author}-{re.sub(r'[^a-zA-Z0-9]', '_', yt.title)}")
                              
    
    # Convert to mp3
    base, ext = os.path.splitext(videofile)
    new_file = base + '.mp3'
    os.rename(videofile, new_file)

    filesize_in_mb = os.stat(new_file).st_size / 1048576
    global total_download_size 
    total_download_size += filesize_in_mb
    print(f"Downloaded '{yt.author} - {yt.title}' Filesize: {round(filesize_in_mb, 2)}MB")
    

def get_channel_video_count():
    templist = scrapetube.get_channel(channel_url=CHANNEL_URL)
    vidcount = 0
    for videos in templist:
        vidcount += 1

    return vidcount



# ------- MAIN ------- #

total_download_size = 0
succesful_downloads = 0
videolist = scrapetube.get_channel(channel_url=CHANNEL_URL)


if MAX_DOWNLOADS == -1:
    MAX_DOWNLOADS = get_channel_video_count()
print(f"Attempting to download {MAX_DOWNLOADS} files...")

for i in range(MAX_DOWNLOADS):
    if total_download_size < DOWNLOAD_LIMIT_IN_MEGABYTES:
        currentId = next(videolist)['videoId']
        downloadvideo(currentId)
        succesful_downloads += 1
    else:
        break

print(f"Succesfully downloaded {succesful_downloads} files.")