import re

f = open("05/crane.txt", "r")
content = f.readlines()

def input():
    stack = [
        ['B', 'P', 'N', 'Q', 'H', 'D', 'R', 'T'],
        ['W', 'B', 'G', 'J', 'T', 'V'],
        ['N', 'R', 'H', 'D', 'S', 'V', 'M', 'Q'],
        ['P', 'Z', 'N', 'M', 'C'],
        ['D', 'Z', 'B'],
        ['V', 'C', 'W', 'Z'],
        ['G', 'Z', 'N', 'C', 'V', 'Q', 'L', 'S'],
        ['L', 'G', 'J', 'M', 'D', 'N', 'V'],
        ['T', 'P', 'M', 'F', 'Z', 'C', 'G']
    ]
    startOfCmd = 0
    while(content[startOfCmd][0] != 'm'):
        startOfCmd = startOfCmd+1
    
    for i in range(startOfCmd, len(content)):
        numbersInString = re.findall(r'\d+', content[i])
        numbers = [eval(j) for j in numbersInString]
        
        for k in range(numbers[0]):
            
            stack[(numbers[2])-1].append(stack[numbers[1]-1].pop((-(numbers[0]))+k)) 
    
    for i in range (9):
        print(stack[i])
              

input()
