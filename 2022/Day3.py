file=open("inputDay3.txt","r")
contents=file.read().split("\n")
commonItemTypes=[]
for rucksackNumber,line in enumerate(contents):
    length=len(line)/2
    comp1=line[:int(length)]
    comp2 = line[int(length):]
    letters1=[]
    appearances1=[]
    letters2 = []
    appearances2 = []
    for char in comp1:
        if(letters1.count(char)==0):
            letters1.append(char)
            appearances1.append(1)
        else:
            appearances1[letters1.index(char)]+=1
    for char in comp2:
        if(letters2.count(char)==0):
            letters2.append(char)
            appearances2.append(1)
        else:
            appearances2[letters2.index(char)]+=1
    for i in range(len(letters1)):
        for j in range(len(letters2)):
            print(f"{letters1[i]}=={letters2[j]} and {appearances1[i]}=={appearances2[j]}")
            if(letters1[i]==letters2[j]):
                commonItemTypes.append(letters1[i])
    print(rucksackNumber)
print(commonItemTypes)
sum=0
for x in commonItemTypes:
    if(ord(x)>64 and ord(x)<97):
        sum+=ord(x)-38
    else:
        sum+=ord(x)-96
print(f"Sum of priorities from rucksacks: {sum}")
#part 2
groups=[]
i=0
currentGroup=[]
commonTypesInGroups=[]
for line in contents:
    currentGroup.append(line)
    i+=1
    if(i%3==0):
        groups.append(currentGroup)
        currentGroup=[]

for groupCount,group in enumerate(groups):
    check=False
    for char in group[0]:
        if(group[1].count(char)!=0 and group[2].count(char) and check==False):
            commonTypesInGroups.append(char)
            check=True
print(commonTypesInGroups)
print(len(commonTypesInGroups))
sum=0
for x in commonTypesInGroups:
    if(ord(x)>64 and ord(x)<97):
        sum+=ord(x)-38
    else:
        sum+=ord(x)-96
print(f"Sum of priorities from groups: {sum}")