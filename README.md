# VideoNames
Little module in python to make a video from a list of names

## Install

pip install -r requirements.txt

## Tutorial

from presentacion import *
nombres=getNames("nomsmentors.csv")
createVideo(nombres,video_name="video.wmv",codec_video="msmpeg4")
