import cv2
import pytesseract
from PyDictionary import PyDictionary
dc = PyDictionary()


path = open("path.txt", "r")
img = cv2.imread(path.read())

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(img,config='tessedit_char_whitelist 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') #11
text=text.replace("\n", "\t")
text=' '.join(text.split())
if(text==""):
    text = pytesseract.image_to_string(img, config='--oem 3 --psm 6')
    text=text.replace("\n", "\t")
    text=' '.join(text.split())
print("Text From The Image : "+text)

splits = text.split()
for split in splits:
    mn=dc.meaning(split)
    if (mn==None):
        pass
    else:
        print(split+" = "+str(mn)+"\n")
