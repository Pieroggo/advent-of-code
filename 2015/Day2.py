file=open("inputDay2.txt","r")
input=file.read()
lines=input.split("\n")
totalWrapping=0
totalRibbon=0
for line in lines:
    measurements=line.split('x')
    a=int(measurements[0])
    b = int(measurements[1])
    c = int(measurements[2])
    totalWrapping+=((2*a*b)+(2*a*c)+(2*b*c))
    totalRibbon+=(a*b*c)
    if(a==min(a,b,c)):
        totalWrapping +=(a*min(b,c))
        totalRibbon+=2*(a+min(b,c))
    elif(b == min(a, b, c)):
        totalWrapping += (b * min(a, c))
        totalRibbon += 2 * (b + min(a, c))
    else:
        totalWrapping += (c * min(b, a))
        totalRibbon += 2 * (c + min(b, a))
print(f"Wrapping: {totalWrapping} Ribbon: {totalRibbon}")