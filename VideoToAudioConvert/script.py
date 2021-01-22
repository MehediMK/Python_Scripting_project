from moviepy.editor import *
filename = input("Enter Video file name with video Extension: ")
savename = input("Enter file Saving name: ")
video_clip = VideoFileClip(filename)
audio_clip = video_clip.audio

audio_clip.write_audiofile(f'{savename}.mp3')
audio_clip.close()
video_clip.close()
print('Successfully Convert!!!')