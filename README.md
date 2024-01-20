This is a simple python script, originally built as a means of building audio datasets for deep learning models, that utilizes scrapetube and pytube to download a specified amount of videos from a channel in mp3 format. Useful for saving music and collecting data. 

Do note that the code is not thoroughly tested, and it's possible some conditions could throw errors, including:
  - 2 or more videos on the channel have the same title (just a filename issue, to be fixed in the future)
  - Large download sizes/amounts that send many requests to YouTube
  - Youtube API changes


To run, specify the channel url and output fold in the "PARAMETERS" section of the script file and adjust the download limits as necessary. 
