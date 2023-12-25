from moviepy.editor import VideoFileClip
 
def converttomp3(mp4file, mp3file):
	video=VideoFileClip(mp4file)
	audio=video.audio
	audio.write_audiofile(mp3file)
	audio.close()
	video.close()
 
converttomp3('video.MOV', 'sound-from-video.wav')