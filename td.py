import cv2
import pytesseract

tesseractLink = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
imgPath = 'ocr2.png' 

pytesseract.pytesseract.tesseract_cmd = tesseractLink
img  = cv2.imread(imgPath)
# converting from bgr to rgb
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img = cv2.GaussianBlur(img, (1, 1), 0)
# img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# creating boxes on the img
# imgH,imgW,_ = img.shape
boxesAsString = pytesseract.image_to_data(img)
# getting direct string


print(boxesAsString)
# print(type(boxesAsString))
# splitedLines = boxesAsString.splitlines()
# t1 = splitedLines[0]
# for x in splitedLines:
#     print('------------------------------------------------------')
#     # print(x)
#     print(x.split())
for count,b in enumerate(boxesAsString.splitlines()):
    b = b.split()
    if count !=0:
        if(len(b)==12):
            print(b[11])
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)

# showing the img in window
img = cv2.resize(img,(960,540))
cv2.imshow('Result', img)
cv2.waitKey(0)