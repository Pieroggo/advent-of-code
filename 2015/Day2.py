file=open("inputDay2.txt","r")
input=file.read()
lines=input.split("\n")
totalWrapping=0
totalRibbon=0
for line in lines:
    measurements=line.split('x')
    print()