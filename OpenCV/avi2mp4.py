import moviepy.editor as mv

clip = mv.VideoFileClip("video.avi")	
clip.write_videofile("video.mp4", fps=1)
