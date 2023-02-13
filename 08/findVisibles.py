f = open("08/input.txt", "r")
content = f.readlines()

visibleTrees = (len(content[0])-1)*2 + (len(content)-2)*2

def checkTops(height, xCoordinate, yCoordinate):
    visibility = True
    for i in range(yCoordinate-1, -1, -1):
        if(content[i][xCoordinate] >= height):
            visibility = False
    return visibility

def checkBottoms(height, xCoordinate, yCoordinate):
    visibility = True
    for i in range(yCoordinate+1, len(content)):
        if((content[i][xCoordinate]) >= height):
            visibility = False
    return visibility

def checkLefts(height, xCoordinate, yCoordinate):
    visibility = True
    for i in range(xCoordinate-1, -1, -1):
        if(content[yCoordinate][i] >= height):
            visibility = False
    return visibility

def checkRights(height, xCoordinate, yCoordinate):
    visibility = True
    for i in range(xCoordinate+1, len(content[0])):
        if(content[yCoordinate][i] >= height):
            visibility = False
    return visibility

for i in range(1, len(content)-1):
    for k in range(1, len(content[0])-2):
        if(checkTops(content[i][k],k,i) 
            or checkBottoms(content[i][k],k,i) 
            or checkLefts(content[i][k],k,i) 
            or checkRights(content[i][k],k,i)):
            visibleTrees = visibleTrees +1

print(visibleTrees)