#part 1 and 2 done simultanously
file=open("inputDay1.txt","r")
input=file.read()
currentFloor=0
isInBasement=False
it=0
iterationOnBasement=0
for char in input:
    it+=1
    if(char=="("):
        currentFloor+=1
    if(char==")"):
        currentFloor-=1
    if(currentFloor<0 and isInBasement==False):
        isInBasement=True
        iterationOnBasement=it
print(f"Santa is on {currentFloor} floor")
print(f"Santa descended into basement on {iterationOnBasement} iteration")
file.close()