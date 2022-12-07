import hashlib
file=open("inputDay4.txt","r")
input=file.read()
#part 1
correctHash=False
i=0
while(not correctHash):
    string=input + str(i)
    hash = hashlib.md5(string.encode()).hexdigest()
    if(hash[5:]=="00000"):
        correctHash=True
    i+=1
print(f"Number needed for 5 0's at the start: {i}")
#part 2
correctHash=False
i=0
while(not correctHash):
    string=input + str(i)
    hash = hashlib.md5(string.encode()).hexdigest()
    if(hash[6:]=="000000"):
        correctHash=True
    i+=1
print(f"Number needed for 6 0's at the start: {i}")