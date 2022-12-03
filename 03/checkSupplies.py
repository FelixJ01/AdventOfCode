f = open("03/rucksack.txt", "r")
content = f.readlines()

sum = 0
for i in range(len(content)):
    sameChar = ""
    part1=content[i][0:int((len(content[i])-1)/2)]
    part2=content[i][int((len(content[i])-1)/2):len(content[i])-1]

    for k in range(len(part1)):
        for j in range(len(part2)):
            if(part1[k] == part2[j]):
                sameChar = part1[k]
    
    if(sameChar.isupper()):
        sum = sum + (ord(sameChar)-38)
    else:
        sum = sum + (ord(sameChar)-96)

print(sum)
        


