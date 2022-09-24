import cv2 as cv

def sketch(image):
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)   
    img_gray_blur = cv.GaussianBlur(img_gray, (5,5), 0)  
    canny_edges = cv.Canny(img_gray_blur, 30, 60)  
    ret, mask = cv.threshold(canny_edges, 240, 255, cv.THRESH_BINARY_INV)  
    return mask


cap= cv.VideoCapture("C:\\Users\\rosha\\OneDrive\\Documents\\ExtraS\\Clubs\\Optizen\\SLAM\\frames\\cam.mp4")
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    frame = sketch(frame)
    cv.imwrite('frames/cam'+str(i)+'.png',frame)
    i+=1

cap.release()
cv.destroyAllWindows()
