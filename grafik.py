import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread('images/employers.jpg')
cv.imshow('kedi', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gri', gray)


gri_grafik = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Gri Tonu')
plt.xlabel('Bins')
plt.ylabel('Piksel numarasi')
plt.plot(gri_grafik)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)