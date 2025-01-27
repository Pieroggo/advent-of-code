file=open("inputDay6.txt","r")
contents=file.read()
i=0
while(i<len(contents)-3):
    check=contents[i:4+i]
    print(check)
    flag=True
    for x in check:
        if(check.count(x)>1):
            flag=False
    if(flag):
        print(f"Key on character {i+4}")
        break
    i+=1
#part 2
i=0
while(i<len(contents)-13):
    check=contents[i:14+i]
    print(check)
    flag=True
    for x in check:
        if(check.count(x)>1):
            flag=False
    if(flag):
        print(f"Key on character {i+14}")
        break
    i+=1
