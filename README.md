This is a simple python script, originally built as a means of building audio datasets for deep learning models, that utilizes scrapetube and pytube to download a specified amount of videos from a channel in mp3 format. Useful for saving music and collecting data. 



To use, first install the required python libraries:
```
pip install scrapetube
```
```
pip install pytube
```

Then, open script.py and specify the channel url and output folder variables in the "PARAMETERS" section at the top of the file. Changing the download limit and max download variables allows you to set a limit on how much the script will download. After this, you're good to run the script.

Do note that some conditions may throw errors, including:
  - 2 or more videos on the channel have the same title (a filename issue, to be fixed in the future)
  - Large download sizes/amounts that send many requests to YouTube
  - Youtube API changes
