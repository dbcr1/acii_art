import cv2 as cv


input = cv.imread(r"6.png")
output = cv.imread(r"output2.png")

input = cv.resize(input, (128*5, 96*5))
output = cv.resize(output, (640, 480))

input = cv.cvtColor(input, cv.COLOR_BGR2GRAY)
cv.imshow("1",input)


input = cv.medianBlur(input, 5)
cv.imshow("2",input)

gb = cv.GaussianBlur(input,(11,11), -1)
tr = cv.adaptiveThreshold(gb,255,cv.ADAPTIVE_THRESH_MEAN_C,\
 cv.THRESH_BINARY,5,2)
cv.imshow("4",tr)

font = cv.FONT_HERSHEY_PLAIN 
pixel_size = 5
for i in range(0, 480, 5 ):
    for j in range(0, 640, 5):
        norm = (((input[i, j] - 255)/(0-255))*1)*4+1
        cv.line(output,(j,i),(j+5,i),(0,0,0),int(norm))
        '''if input[i, j] < 190:
            cv.putText(output, '-', (j,i),font, (pixel_size * 0.075) *2 , (0,0,0), 2)
            #cv.rectangle(output, (j,i),(j+5,i+5), (0,0,0), -1)
        else:
            cv.putText(output, '-', (j,i),font, (pixel_size * 0.075) *2 , (255,255,255), 2)
            #cv.rectangle(output, (j,i),(j+5,i+5), (255,255,255), -1)'''


cv.imshow("3",output)
cv.waitKey(0)
print (128*5, 96*5)
    