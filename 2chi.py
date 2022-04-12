import cv2

filename = "red.jpg"
gry = cv2.imread(filename,0)
cv2.imwrite('gray.jpg', gry)