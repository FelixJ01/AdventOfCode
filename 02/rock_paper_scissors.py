f = open("02/rps.txt", "r")
content = f.readlines()
point_dict = {'A':1, 'X':1, 'B':2, 'Y':2, 'C':3, 'Z':3}
sum = 0
def getWinner(opponent, me):
    me = me[0]
    if((opponent == "A" and me == "Y") or (opponent == "B" and  me == "Z") or (opponent == "C" and  me == "X")):
        return 6
    if((opponent == "A" and  me == "Z") or(opponent == "B" and  me == "X") or (opponent == "C" and  me == "Y")):
        return 0
    else:
        return 3    
for i in range(len(content)):
    sum = sum + getWinner(content[i].split(" ")[0], content[i].split(" ")[1]) + point_dict[content[i].split(" ")[1][0]] 
print(sum)

