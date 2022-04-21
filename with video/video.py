import cv2 as cv

video = cv.VideoCapture(0)

if (video.isOpened() == False):
	print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

result = cv.VideoWriter('frames/cam.mp4',
						cv.VideoWriter_fourcc(*'MP4V'),
						10, size)
	

while(True):
	ret, frame = video.read()

	if ret == True:

		result.write(frame)

		cv.imshow('Frame', frame)

		if cv.waitKey(1) & 0xFF == ord('s'):
			break
	else:
		break

video.release()
result.release()
	
cv.destroyAllWindows()

print("The video was successfully saved")