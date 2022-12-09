file=open("inputDay2.txt","r")
contents=file.read().split("\n")
score=0
typeMatchup={"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3}
for line in contents:
    actions=line.split()
    outcome=typeMatchup.get(actions[0])-typeMatchup.get(actions[1])
    score+=typeMatchup.get(actions[1])
    if(outcome==0):
        score+=3
    elif(outcome==2 or outcome==-1):
        score+=6
print(f"Total score: {score}")
#part 2
realScore=0
for line in contents:
    actions = line.split()
    outcome=typeMatchup.get(actions[1])
    if(outcome==3):
        realScore+=6
        if(typeMatchup.get(actions[0])==3):
            realScore+=1
        else:
            realScore+=typeMatchup.get(actions[0])+1
    elif(outcome==2):
        realScore+=3+typeMatchup.get(actions[0])
    else:
        if (typeMatchup.get(actions[0])==1):
            realScore+=3
        else:
            realScore += typeMatchup.get(actions[0]) - 1
print(f"Real total score: {realScore}")