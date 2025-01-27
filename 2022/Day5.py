file=open("inputDay5.txt","r")
contents=file.read().split("\n")
i=0
startingStateLines=[]
manualLines=[]
while(contents[i]!=""):
    startingStateLines.append((contents[i]))
    i+=1
while(i<len(contents)):
    manualLines.append(contents[i])
    i+=1
numberOfColumns=0
for char in startingStateLines[-1]:
    if(char!=" "):
        if(numberOfColumns<int(char)):
            numberOfColumns=int(char)
i=len(startingStateLines)-1
columns=[]
for e in range(numberOfColumns):
    columns.append([])
while(i>0):
    strin=""
    for count,char in enumerate(startingStateLines[i-1]):
        strin+=char
    print(strin)
    i-=1
i=len(startingStateLines)-2
index=1
x=0
while(i>=0):
    while(index<len(startingStateLines[i])):
        if(startingStateLines[i][index]!=" "):
            columns[x].append(startingStateLines[i][index])
        index+=4
        x+=1
    i-=1
    x=0
    index=1
print(columns)
#parsed to columns
manualLines.pop(0)
for line in manualLines:
    parts=line.split(" ")
    n=int(parts[1])
    for x in range(n):
        columns[int(parts[5])-1].append(columns[int(parts[3])-1].pop(-1))
print(columns)
topValues=[]
for column in columns:
    topValues+=[column[-1]]
print(topValues)
#part 2
i=0
startingStateLines=[]
manualLines=[]
while(contents[i]!=""):
    startingStateLines.append((contents[i]))
    i+=1
while(i<len(contents)):
    manualLines.append(contents[i])
    i+=1
numberOfColumns=0
for char in startingStateLines[-1]:
    if(char!=" "):
        if(numberOfColumns<int(char)):
            numberOfColumns=int(char)
print(f"number of columns: {numberOfColumns}")
i=len(startingStateLines)-1
columns=[]
for e in range(numberOfColumns):
    columns.append([])
print(columns)
while(i>0):
    strin=""
    for count,char in enumerate(startingStateLines[i-1]):
        strin+=char
    print(strin)
    i-=1
i=len(startingStateLines)-2
index=1
x=0
while(i>=0):
    while(index<len(startingStateLines[i])):
        if(startingStateLines[i][index]!=" "):
            columns[x].append(startingStateLines[i][index])
        index+=4
        x+=1
    i-=1
    x=0
    index=1
print(columns)
manualLines.pop(0)
for line in manualLines:
    parts=line.split(" ")
    n=int(parts[1])
    tmpStack=[]
    for x in range(n):
        tmpStack.append(columns[int(parts[3])-1].pop(-1))
    for x in range(n):
        columns[int(parts[5])-1].append(tmpStack.pop(-1))
print(columns)
topValues=[]
for column in columns:
    topValues+=[column[-1]]
print(topValues)