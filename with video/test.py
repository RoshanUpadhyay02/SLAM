import cv2 as cv

def sketch(image):
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    img_gray_blur = cv.GaussianBlur(img_gray, (5,5), 0)
    
    canny_edges = cv.Canny(img_gray_blur, 30, 60)
    
    ret, mask = cv.threshold(canny_edges, 240, 255, cv.THRESH_BINARY_INV)
    
    return mask


cam = cv.VideoCapture(0)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error,
# show result
if result:

	# showing result, it take frame name and image
	# output
	cv.imshow("GeeksForGeeks", sketch(image))

	# saving image in local storage
	cv.imwrite("GeeksForGeeks.png", sketch(image))
    
	# If keyboard interrupt occurs, destroy image
	# window

image = cv.imread('GeeksForGeeks.png')
up_width = 1200
up_height = 600
up_points = (up_width, up_height)
resized_up = cv.resize(image, up_points, interpolation= cv.INTER_CUBIC)

cv.imshow('Resized Up image by defining height and width', resized_up)
cv.imwrite("GeeksForGeeks.png", resized_up)
cv.waitKey(0)
cv.destroyWindow("GeeksForGeeks")