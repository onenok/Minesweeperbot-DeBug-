import pyautogui as pgui
from win32api import GetSystemMetrics as gsm

startX = ((((gsm(0)-1)/2)-618.5)/2)+1.5
startY = (gsm(1)-730)/2+172

numColumns = 24
numRows = 20

pixel = 25
halfPixel = pixel/2
pixelCoordinate = (round(pixel*0.5), round(pixel*0.27)-1)

def screenshot():
    pgui.screenshot("board.png", region=(startX, startY, 600, 500))


def moveMouseAway():
    pgui.moveTo(1520, 670)


def getXCoordinate(column):
    return column*pixel+startX


def getYCoordinate(row):
    return row*pixel+startY


def cellScreenshot(filename, row, column):
    pgui.screenshot(filename, region=(getXCoordinate(row),
                    getYCoordinate(column), pixel, pixel))


def boardXCoord(column):
    return column*pixel


def boardYCoord(row):
    return row*pixel


def leftClick(column, row):
    pgui.click(x=getXCoordinate(column)+pixelCoordinate[0], y=getYCoordinate(row)+pixelCoordinate[1])


def rightClick(column, row):
    pgui.rightClick(x=getXCoordinate(column)+pixelCoordinate[0], y=getYCoordinate(row)+pixelCoordinate[1])
