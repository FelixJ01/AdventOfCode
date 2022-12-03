f = open("03/rucksack.txt", "r")
content = f.readlines()

sum = 0

def getValue(sameChar):
    sum = 0
    if(sameChar.isupper()):
        sum = sum + (ord(sameChar)-38)
    else:
        sum = sum + (ord(sameChar)-96)
    return sum


for i in range(len(content)):
    if(i % 3 == 0):
        sameChar = ''
        for j in range(len(content[i])):
            if(content[i][j] in content[i+1] and content[i][j] in content[i+2] and sameChar == ''):
                sameChar=content[i][j]
                sum = sum + getValue(content[i][j])
print(sum)