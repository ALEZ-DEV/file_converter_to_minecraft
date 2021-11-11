"""
get the mean color value of the all texture in a folder and create a .csv file

credit - ALEZ
github - https://github.com/Raidersfocus
"""

import glob
import cv2
import csv

folder = glob.glob("C:\\Users\\Raide\\OneDrive\\Documents\\Bureau\\PythonCode\\MinecraftVideo\\data\\*.png")
currentHeight = 0
currentWidth = 0
pixel = 0
Color = []

def moyenne(list) :
    Num = 0
    for listN in range(len(list)):
        Num = Num + list[listN]
    final = Num / len(list)
    return final

for i in range(len(folder)):
    image = cv2.imread(folder[i])
    RGB = []
    mb = []
    mg = []
    mr = []
    finalRGB = []
    height, width, channel = image.shape

    while(True):
        if currentHeight < height :
            while(True):
                if currentWidth < width :
                    pixel += 1
                    blue, green, red = image[currentWidth, currentHeight]
                    RGB.append([blue, green, red])
                    currentWidth += 1
                    print(blue, green, red)
                else :
                    currentWidth = 0
                    break
            currentHeight += 1
        else:
            currentHeight = 0
            break

    for n in range(len(RGB)):
        #mb = moyenne blue, mg = moyenne green, mr = moyenne red
        Mblue, Mgreen, Mred = RGB[n]
        mb.append(Mblue)
        mg.append(Mgreen)
        mr.append(Mred)
    Blue = moyenne(mb)
    Green = moyenne(mg)
    Red = moyenne(mr)
    finalRGB.append(int(Blue))
    finalRGB.append(int(Green))
    finalRGB.append(int(Red))
    Color.append(finalRGB)
        
with open("BlockColor.csv", "w", newline="") as csv_file :
    csv_writer = csv.writer(csv_file, delimiter=",")
    
    for n in range(len(folder)):
        blockName = folder[n].replace("C:\\Users\\Raide\\OneDrive\\Documents\\Bureau\\PythonCode\\MinecraftVideo\\data\\","")
        blockName = blockName.replace(".png","")
        body = [blockName]
        blockColor = Color[n]
        body.append(blockColor[0])
        body.append(blockColor[1])
        body.append(blockColor[2])
        csv_writer.writerow(body)
    print("writed")


print("Finished")