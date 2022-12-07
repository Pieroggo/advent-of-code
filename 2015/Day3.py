file=open("inputDay3.txt","r")
input=file.read()
#part 1
housesVisited=[[0,0]]
currentHouse=[0,0]
for char in input:
    if (char=="^"):
        currentHouse[1]+=1
    if (char == "v"):
        currentHouse[1] -= 1
    if (char == ">"):
        currentHouse[0] += 1
    if (char == "<"):
        currentHouse[0] -= 1
    if(housesVisited.count([currentHouse[0],currentHouse[1]])==0):
        housesVisited.append([currentHouse[0],currentHouse[1]])
print(f"Houses visited without Robo: {len(housesVisited)}")
#part 2
housesVisited=[]
currentSantaHouse=[0,0]
currentRoboHouse=[0,0]
it=0
for char in input:
    it+=1
    if (char=="^"):
        if(it%2==1):
            currentSantaHouse[1]+=1
        else:
            currentRoboHouse[1]+=1
    if (char == "v"):
        if (it % 2 == 1):
            currentSantaHouse[1] -= 1
        else:
            currentRoboHouse[1] -= 1
    if (char == ">"):
        if (it % 2 == 1):
            currentSantaHouse[0] += 1
        else:
            currentRoboHouse[0] += 1
    if (char == "<"):
        if (it % 2 == 1):
            currentSantaHouse[0] -= 1
        else:
            currentRoboHouse[0] -= 1
    if(housesVisited.count([currentSantaHouse[0],currentSantaHouse[1]])==0):
            housesVisited.append([currentSantaHouse[0],currentSantaHouse[1]])
    if (housesVisited.count([currentRoboHouse[0], currentRoboHouse[1]]) == 0):
        housesVisited.append([currentRoboHouse[0],currentRoboHouse[1]])
print(f"Houses visited with Robo: {len(housesVisited)}")