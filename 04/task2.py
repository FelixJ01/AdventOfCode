f = open("04/id.txt", "r")
content = f.readlines()

sum = 0

for i in range(len(content)):
    firstPart = content[i].split(',')[0]
    firstStart = int(firstPart.split('-')[0])
    firstEnd = int(firstPart.split('-')[1])

    secondPart= content[i].split(',')[1]
    secondStart = int(secondPart.split('-')[0])
    secondEnd = int(secondPart.split('-')[1].replace('\n',''))

    if(
        (firstStart >= secondStart and firstStart <= secondEnd)
        or (firstEnd >= secondStart and firstEnd <= secondEnd)
        or (secondStart >= firstStart and secondStart <= firstEnd)
        or (secondEnd >= firstStart and secondEnd <= firstEnd)
    ):
        sum = sum +1

print(sum)