"""
generate a mincraft commande from image to convert a image wall in minecraft

credit - ALEZ
github - https://github.com/Raidersfocus
"""

import csv
import cv2

#initialize the variable you need
blockName = []
blockBlue = []
blockGreen = []
blockRed = []
NumOfBlock = 0
frame = cv2.imread("thumb-108917.png")
height, width, channel = frame.shape
NumOfPixel = height * width
choosedBlockName = []
firstPart = "summon falling_block ~ ~.5 ~ {Time:1,BlockState:{Name:redstone_block},Passengers:[{id:armor_stand,Health:0,Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:[{id:command_block_minecart,Command:'gamerule commandBlockOutput false'},{id:command_block_minecart,Command:'data merge block ~ ~-2 ~ {auto:0}'},"
lastPart = "{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:-fill ~ ~ ~ ~ ~-2 ~ air-}'},{id:command_block_minecart,Command:'setblock ~ ~ ~ air'}]}]}]}"

#read the .csv file for get the all texture color
with open("BlockColor.csv", "r") as file :
    reader = csv.reader(file)
    for i in reader :
        blockName.append(i[0])
        blockBlue.append(int(i[1]))
        blockGreen.append(int(i[2]))
        blockRed.append(int(i[3]))
    NumOfBlock = len(blockName)

#function for get some of a number
def environ(a, b, difference):
    if a <= b + difference and a > b :
        c = True
    elif a >= b - difference and a < b :
        c = True
    elif a == b :
        c = True
    else:
        c = False
    return c
    

#this function check all pixel color and get which pixel go with which texture
def checkPixelBlock():
    height, width, channel = frame.shape
    currentHeight = 0
    currentWidth = 0
    pixel = height * width
    checkPixelpourcent = 100 / pixel
    frameBlue = []
    frameGreen = []
    frameRed = []

    while(True):
        if currentHeight < height :
            while(True):
                if currentWidth < width :
                    blue, green, red = frame[currentWidth, currentHeight]
                    frameBlue.append(blue)
                    frameGreen.append(green)
                    frameRed.append(red)
                    currentWidth += 1
                    print(f"{int(checkPixelpourcent)} %")
                    checkPixelpourcent += 100 / pixel
                else :
                    currentWidth = 0
                    break
            currentHeight += 1
        else :
            break
    for n in range(len(frameBlue)):
        for c in range(NumOfBlock) :
            PB = environ(frameBlue[n], blockBlue[c], 26)
            PG = environ(frameGreen[n], blockGreen[c], 26)
            PR = environ(frameRed[n], blockRed[c], 26)
            if (PB and PG and PR) == True :
                choosedBlockName.append(blockName[c])
                break
        print(f"find block for pixel {n}")    
        
#function commandReplaceCaracter() replace the - to " and the ! to '       
def commandReplace(command) :

    command1 = command.replace("-",'"')
    command2 = command1.replace("#","{")
    replaced = command2.replace("!","'")
    return replaced

#this function generate the minecraft commande           
def CommandeGenerator() :
    
    listOfCommand = []
    completedCommand = firstPart
    

    for i in range(height) :
        a = 0
        for n in range(width) :
            
            command = choosedBlockName
            commandPart = commandReplace(f"#id:command_block_minecart,Command:'fill ~{i} ~ ~{n} ~{i} ~ ~{n} " + command[a] + "'},")
            listOfCommand.append(commandPart)
            a += 1

    for num in range(len(listOfCommand)) :
        completedCommand = completedCommand + listOfCommand[num]
    completedCommand = completedCommand + commandReplace(lastPart)

    return completedCommand

checkPixelBlock()
#write a .txt file with the minecraft command in it 
commandFile = open("command.txt", "w+")
commandFile.write(CommandeGenerator())
commandFile.close
print("text file is writed !")