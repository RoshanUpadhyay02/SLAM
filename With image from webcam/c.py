import cv2 as cv

def sketch(image):
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    img_gray_blur = cv.GaussianBlur(img_gray, (5,5), 0)
    
    canny_edges = cv.Canny(img_gray_blur, 30, 60)
    
    ret, mask = cv.threshold(canny_edges, 240, 255, cv.THRESH_BINARY_INV)
    
    return mask


cam = cv.VideoCapture(0)

result, image = cam.read()

if result:
	
	cv.imwrite("img.jpg", sketch(image))

image = cv.imread('img.jpg')
up_width = 1200
up_height = 600
up_points = (up_width, up_height)
resized_up = cv.resize(image, up_points, interpolation= cv.INTER_CUBIC)

cv.imwrite("img.jpg", resized_up)
cv.waitKey(0)
