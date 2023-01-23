f = open("06/input.txt", "r")
content = f.readlines()

def findMarker():
    parts=[]
    for i in range(len(content[0])):
        if(len(parts) == 4):
            print(i+3)
            break
        parts = [content[0][i]]
        for k in range(1,4):
            test = content[0][i+k]
            if(content[0][i+k] not in parts):
                parts.append(content[0][i+k])
            else:
                break

findMarker()