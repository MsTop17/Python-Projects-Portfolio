from moviepy import VideoFileClip
cvt_video = VideoFileClip("my file.mp4")

ext_audio = cvt_video.audio
ext_audio.write_audiofile("extracted_audio.mp3")