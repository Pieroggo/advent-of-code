file=open("inputDay1.txt","r")
contents=file.read().split("\n")
calories=0
elves=[]
for x in contents:
    if(x==""):
        elves.append(calories)
        calories = 0
    else:
        calories += int(x)
chonkyElf=0
amountOfChonkyElfs=0
chonkyElves=[]
while(amountOfChonkyElfs<3):
    for elf in elves:
     if(chonkyElf<elf):
        chonkyElf=elf
    for elf in elves:
        if(chonkyElf==elf):
            chonkyElves.append(elves.pop(elves.index(elf)))
            chonkyElf=0
            amountOfChonkyElfs+=1
print(f"Top 3 chonkiest elves: {chonkyElves[0]}, {chonkyElves[1]} and {chonkyElves[2]} Sum of calories: {chonkyElves[0]+chonkyElves[1]+chonkyElves[2]}")