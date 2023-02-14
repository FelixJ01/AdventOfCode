f = open("08/input.txt", "r")
content = f.readlines()

visibleTrees = (len(content[0])-1)*2 + (len(content)-2)*2

def checkTops(height, xCoordinate, yCoordinate):
    visibleTop = 0
    for i in range(yCoordinate-1, -1, -1):
        if(content[i][xCoordinate] >= height):
            visibleTop = visibleTop + 1
            break
        else:
            visibleTop = visibleTop + 1
    return visibleTop

def checkBottoms(height, xCoordinate, yCoordinate):
    visibleBottom = 0
    for i in range(yCoordinate+1, len(content)):
        if((content[i][xCoordinate]) >= height):
            visibleBottom = visibleBottom +1
            break
        else:
            visibleBottom = visibleBottom + 1
    return visibleBottom

def checkLefts(height, xCoordinate, yCoordinate):
    visibleLeft = 0
    for i in range(xCoordinate-1, -1, -1):
        if(content[yCoordinate][i] >= height):
            visibleLeft = visibleLeft + 1
            break
        else:
            visibleLeft = visibleLeft + 1 
    return visibleLeft

def checkRights(height, xCoordinate, yCoordinate):
    visibleRight = 0
    for i in range(xCoordinate+1, len(content[0])-1):
        if(content[yCoordinate][i] >= height):
            visibleRight = visibleRight +1
            break
        else:
            visibleRight = visibleRight + 1
    return visibleRight

result = 0


for i in range(1, len(content)-1):
    for k in range(1, len(content[0])-2):
        scenicScore = checkTops(content[i][k],k,i) * checkBottoms(content[i][k],k,i) * checkLefts(content[i][k],k,i) * checkRights(content[i][k],k,i)
        if(scenicScore > result):
            result = scenicScore

print(result)