import cv2 as cv
import video
import exframes
import count

i = 0

while(i != count.count):

    img = cv.imread('frames/cam'+str(i)+'.png', cv.IMREAD_COLOR)
    up_width = 1200
    up_height = 600
    up_points = (up_width, up_height)
    resized_up = cv.resize(img, up_points, interpolation= cv.INTER_CUBIC)

    cv.imwrite('frames/cam'+str(i)+'.png', resized_up)

    i+=1
    
cv.waitKey(0)
cv.destroyAllWindows()




