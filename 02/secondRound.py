f = open("02/rps.txt", "r")
content = f.readlines()

point_dict = {'X': 0, 'Y': 3, 'Z':6}
play_dict = {"C": 3, "A":1, "B":2}

# A = Rock
# B = Paper
# C = Scissor

# X = Verlieren
# Y = Unentschieden
# Z = Gewinnen
sum = 0

for i in range(len(content)):
    sum = sum + point_dict[content[i].split(" ")[1][0]]
    if(point_dict[content[i].split(" ")[1][0]] == 3):
        sum = sum + play_dict[content[i].split(" ")[0]]
    elif(point_dict[content[i].split(" ")[1][0]] == 0):
        if(content[i].split(" ")[0] == "A"):
            sum = sum + 3
        if(content[i].split(" ")[0] == "B"):
            sum = sum + 1
        if(content[i].split(" ")[0] == "C"):
            sum = sum + 2
    elif(point_dict[content[i].split(" ")[1][0]] == 6):
        if(content[i].split(" ")[0] == "A"):
            sum = sum + 2
        if(content[i].split(" ")[0] == "B"):
            sum = sum + 3
        if(content[i].split(" ")[0] == "C"):
            sum = sum + 1
print(sum)
    
