import pickle
import numpy as np
import time
from PIL import Image
import sys
from screenshot import *
from cellColors import pixelCoordinate
from cellColors import cellTypes
colors = pickle.load(open("colors.p", "rb"))
errors = 0
global unsolved
unsolved = []

def getCode(rgb, column, row):
    for code in cellTypes:
        if rgb == colors[code]:
            if int(code) > 10:
                print("type:"+code[0]+"          ")
                print("\n")
                return int(code[0])
            else:
                print("type:"+code+"          ")
                print("\n")
                return int(code)
        else:
            print("type:loading.",end="\r")
    global errors
    errors += 1
    cellScreenshot('errors/1.png', column, row)
    cellScreenshot('errors/2.png', column, row)
    cellScreenshot('errors/3.png', column, row)
    cellScreenshot('errors/4.png', column, row)
    cellScreenshot('errors/5.png', column, row)
    moveMouseAway()
    screenshot()
    board = Image.open("board.png")
    boardRGB = board.convert("RGB")
    RGB = boardRGB.getpixel((300, 250))
    if RGB == (101, 181, 222):
        print("type:WRONG               \n")
        sys.exit("OH!GET IT WRONG")
    if RGB == (142, 204, 57):
        print("type:SOLVED              \n")  
        sys.exit("           ▄▄\n           █░█\n           █░█\n          █░░█\n         █░░░█\n███████▄▄█░░░██████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█████░░░░░░░░█\n██████▀   ▀▀██████▀▀")
        
    time.sleep(1)
    print("type:loading..",end="\r")
    
    moveMouseAway()
    screenshot()
    board = Image.open("board.png")
    boardRGB = board.convert("RGB")
    RGB = boardRGB.getpixel((300, 250))
    if RGB == (101, 181, 222):
        print("type:WRONG              \n")
        sys.exit("OH!GET IT WRONG")
    if RGB == (142, 204, 57):
        print("type:SOLVED              \n")
        sys.exit("           ▄▄\n           █░█\n           █░█\n          █░░█\n         █░░░█\n███████▄▄█░░░██████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█████░░░░░░░░█\n██████▀   ▀▀██████▀▀")
        
    time.sleep(1)
    print("type:loading...",end="\r")
    
    moveMouseAway()
    screenshot()
    board = Image.open("board.png")
    boardRGB = board.convert("RGB")
    RGB = boardRGB.getpixel((300, 250))
    if RGB == (101, 181, 222):
        print("type:WRONG              \n")
        sys.exit("OH!GET IT WRONG")
    if RGB == (142, 204, 57):
        print("type:SOLVED              \n")
        sys.exit("           ▄▄\n           █░█\n           █░█\n          █░░█\n         █░░░█\n███████▄▄█░░░██████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█████░░░░░░░░█\n██████▀   ▀▀██████▀▀")
        
    time.sleep(1)
    print("type:loading.  ",end="\r")
    
    moveMouseAway()
    screenshot()
    board = Image.open("board.png")
    boardRGB = board.convert("RGB")
    RGB = boardRGB.getpixel((300, 250))
    if RGB == (101, 181, 222):
        print("type:WRONG              \n")
        sys.exit("OH!GET IT WRONG")
    if RGB == (142, 204, 57):
        print("type:SOLVED              \n")
        sys.exit("           ▄▄\n           █░█\n           █░█\n          █░░█\n         █░░░█\n███████▄▄█░░░██████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█████░░░░░░░░█\n██████▀   ▀▀██████▀▀")
        
    time.sleep(1)
    print("type:loading..",end="\r")
    
    moveMouseAway()
    screenshot()
    board = Image.open("board.png")
    boardRGB = board.convert("RGB")
    RGB = boardRGB.getpixel((300, 250))
    if RGB == (101, 181, 222):
        print("type:WRONG               \n")
        sys.exit("OH!GET IT WRONG")
    if RGB == (142, 204, 57):
        print("type:SOLVED              \n")
        sys.exit("           ▄▄\n           █░█\n           █░█\n          █░░█\n         █░░░█\n███████▄▄█░░░██████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█████░░░░░░░░█\n██████▀   ▀▀██████▀▀")
        
    time.sleep(1)
    print("type:loading...",end="\r")
    
    moveMouseAway()
    screenshot()
    board = Image.open("board.png")
    boardRGB = board.convert("RGB")
    RGB = boardRGB.getpixel((300, 250))
    if RGB == (101, 181, 222):
        print("type:WRONG               \n")
        sys.exit("OH!GET IT WRONG")
    if RGB == (142, 204, 57):
        print("type:SOLVED              \n")
        sys.exit("           ▄▄\n           █░█\n           █░█\n          █░░█\n         █░░░█\n███████▄▄█░░░██████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░█\n▓▓▓▓▓▓█████░░░░░░░░█\n██████▀   ▀▀██████▀▀")
    
    print("type:ERROR     \n")   
    sys.exit("MatchError: unknow cell("+str(column+1)+","+str(row+1)+")")


def getBoardArray():
    moveMouseAway()
    screenshot()

    #time.sleep(1)
    board = Image.open("board.png")
    boardRGB = board.convert("RGB")
    global unsolved
    unsolved = []
    result = []
    
    for row in range(numRows):
        arr = []
        for column in range(numColumns):
            print("X:"+str(column+1)+",Y:"+str(row+1))
            xCoordinate = boardXCoord(column) + pixelCoordinate[0]
            yCoordinate = boardYCoord(row) + pixelCoordinate[1]
            pixelValue = boardRGB.getpixel((xCoordinate, yCoordinate))
            print("R:"+str(pixelValue[0])+"\n"+"G:"+str(pixelValue[1])+"\n"+"B:"+str(pixelValue[2]))
            gh = getCode(pixelValue, column, row)
            if gh == 9:
                unsolved.append([column,row])
            arr.append(gh)
        
        result.append(arr)
    print("\n")
    print(np.array(result))
    print("\n")
    board.close()

    return np.array(result)

    #getBoardArray()
