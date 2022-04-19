import cv2 as cv

cap = cv.VideoCapture(0)

# если флаг full_symbol установлен в True, то используется 
# следующая таблица acii https://voltiq.ru/wp-content/uploads/ascii-code-table.jpg
# если стоит флаг False, то используются только те символы 
# которые записаны в переменную symbol, справо налево уменьшается яркость пикселя
full_symbol = False
symbol = '01'

# если флаг color установлен в True, то цвет символа будет 
# такой как цвет пикселя в исходной изображении.
# если флаг False, то используется цвет, который указан в 
# в переменной color_text. Цвет кодируется в формате Blue, Green, Red
color = True
color_text = (255,255,255)


# чем меньше pixel_size, тем больше детализация на выходе, но 
# при слишком маленьком значении возможно падение fps на выходе
# рекомендуемые значения от 5 до 25
pixel_size = 15

# размер выходного изображения
# при больших значениях данных переменных и маленьком значении pixel_size
# возможны падение fps на выходе
height = 480
width = 640


while True:
    output = cv.imread(r"output.png")
    _,picture = cap.read()
    picture = cv.resize(picture, (width,height))
    picture = cv.GaussianBlur(picture,(25,25),1)
    
    output = cv.resize(output, (int(picture.shape[1]),int(picture.shape[0])))
    #cv.imshow('input', picture)
    picture_gray = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)
    font = cv.FONT_HERSHEY_PLAIN 

    for i in range(0,picture_gray.shape[1]-1, pixel_size):
        for j in range(0,picture_gray.shape[0]-1, pixel_size):
            if color == True:
                color_text = (int(picture[j][i][0]),int(picture[j][i][1]),int(picture[j][i][2]))
            if full_symbol == True:
                if int(picture_gray[j][i]/2) < 33:
                    cv.putText(output, '.', (i,j),font, (pixel_size * 0.075) *2 , color_text, 2)
                    continue

                cv.putText(output, chr(int(picture_gray[j][i]/2)-1), (i,j),font,pixel_size * 0.075, color_text, 1)
                
            else:
                cv.putText(output, symbol[int(picture_gray[j][i]/(255/len(symbol)))-1], (i,j),font, pixel_size * 0.075, color_text, 1)
    
    cv.imshow('input2', output)


    if cv.waitKey(1) == 27:
        break