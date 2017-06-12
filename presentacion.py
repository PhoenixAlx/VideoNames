from moviepy.editor import *
import csv
def getNames(title):
    salida=[]
    with open(title,encoding='ISO-8859-1') as csvfile:
        namereader = csv.reader(csvfile, delimiter=',')
        for row in namereader:
            salida.append(row[0])

    
    return salida
#video = VideoFileClip("myHolidays.mp4").subclip(50,60)
#https://github.com/Zulko/moviepy/issues/400

# Make the text. Many more options are available.
def getClips(names):
    salida=[]
    
    for n in names:
        txt_clip = ( TextClip(n,fontsize=70,color='red',bg_color='white')
                 .set_position('center')
                 .set_duration(0.7)
                  )
        salida.append(txt_clip);
    
    return salida
def createVideo(nombres,video_name,codec_video):
    final_clip = concatenate(getClips(nombres), method = "compose")
    final_clip.write_videofile(video_name,fps=25,codec=codec_video) # Many options...
    

#clip =ImageClip("fondo.jpg")
#video = CompositeVideoClip([clip,final_clip],use_bgclip=True)
#result = CompositeVideoClip(getClips(nombres)) # Overlay text on video

