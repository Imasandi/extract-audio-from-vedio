import moviepy.editor

# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip("E:\python projects new\extract audeo from a vedio\Mera Yaar.mp4 ")

audio = video.audio

# Replace the parameter with the location along with filename
audio.write_audiofile("E:\Mera Yaar.mp3")
