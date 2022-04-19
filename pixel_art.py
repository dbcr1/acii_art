from doctest import FAIL_FAST
import cv2 as cv

cap = cv.VideoCapture(0)

# чем меньше pixel_size, тем больше детализация на выходе, но 
# при слишком маленьком значении возможно падение fps на выходе
# рекомендуемые значения от 4 до 26
# значения четные
pixel_size = 7

# размер выходного изображения
# при больших значениях данных переменных и маленьком значении pixel_size
# возможны падение fps на выходе
height = 960
width = 1280


while True:
    output = cv.imread(r"output.png")
    _,picture = cap.read()
    picture = cv.resize(picture, (width,height))
    picture = cv.GaussianBlur(picture,(25,25),1)
    
    output = cv.resize(output, (int(picture.shape[1]),int(picture.shape[0])))
    picture_gray = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)
    font = cv.FONT_HERSHEY_PLAIN 

    for i in range(0,picture_gray.shape[1]-1, pixel_size):
        for j in range(0,picture_gray.shape[0]-1, pixel_size):
            cv.rectangle(output, 
            (int(i - pixel_size/2),int(j - pixel_size/2)), 
            (int(i + pixel_size/2),int(j + pixel_size/2)), 
            (int(picture[j][i][0]),int(picture[j][i][1]),int(picture[j][i][2])),
            -1)
    cv.imshow('input2', output)


    if cv.waitKey(1) == 27:
        break