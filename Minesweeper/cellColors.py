from PIL import Image
import pickle
from screenshot import pixel
from screenshot import halfPixel
import os

cellTypes = ["0", "00", "1", "2", "3", "4",
             "44", "5", "6", "66", "7", "9", "99", "-1"]

cellColors = {}

pixelCoordinate = (round(pixel*0.5), round(pixel*0.27)-1)


for code in cellTypes:
    examinedImg = Image.open("skin/"+code+"/2.png")
    examinedImgRGB = examinedImg.convert("RGB")
    pixelColor = examinedImgRGB.getpixel(pixelCoordinate)

    cellColors[code] = pixelColor


pickle.dump(cellColors, open("colors.p", "wb"))

print(cellColors)
print("\n")

