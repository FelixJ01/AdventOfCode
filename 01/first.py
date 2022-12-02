f = open("01/elfen.txt", "r")
content = f.readlines()
highestCal = 0
middleCal= 0
lowestCal=0
sum = 0
def toInt(line):
    result = 0
    count = len(line)-1
    for i in range(len(line)-1):
        result = result + int(line[i]) * 10**(count-1)
        count = count -1
    return result

for i in range(len(content)):
    if(content[i] != "\n"):
        sum = sum + toInt(content[i])
    else:  
        if(sum > highestCal):
            lowestCal = middleCal
            middleCal = highestCal
            highestCal = sum
        elif(sum > middleCal):
            lowestCal = middleCal
            middleCal = sum
        elif(sum > lowestCal):
            lowestCal = sum
        sum = 0
print(highestCal+middleCal+lowestCal)







