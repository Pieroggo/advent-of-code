file=open("inputDay4.txt","r")
contents=file.read().split("\n")
inclusionCounter=0
overlappingCounter=0
i=0
for line in contents:
    ranges=line.split(",")
    delims1=ranges[0].split("-")
    delims2=ranges[1].split("-")
    print(f"{delims1[0]} - {delims1[1]} and {delims2[0]} - {delims2[1]} inclusive?")
    if(int(delims1[0])>=int(delims2[0]) and int(delims1[1])<=int(delims2[1])):
            inclusionCounter+=1
            print("taken")
    elif (int(delims2[0]) >= int(delims1[0]) and int(delims2[1]) <= int(delims1[1])):
            inclusionCounter += 1
            print("taken")
    i+=1
print(f"Inclusive ranges: {inclusionCounter}")
for line in contents:
    ranges=line.split(",")
    delims1=ranges[0].split("-")
    delims2=ranges[1].split("-")
    if(int(delims1[1])>=int(delims2[0]) and int(delims1[1])<=int(delims2[1])):
        overlappingCounter+=1
    elif(int(delims2[1])>=int(delims1[0]) and int(delims2[1])<=int(delims1[1])):
        overlappingCounter+=1
    else:
        print(f"{delims1[0]} - {delims1[1]} and {delims2[0]} - {delims2[1]} overlapping?")
print(f"Overlapping ranges: {overlappingCounter}")