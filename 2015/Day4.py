import hashlib
file=open("inputDay4.txt","r")
input=file.read()
correctHash=False
i=0
while(not correctHash):
    string=input + str(i)
    hash = hashlib.md5(string.encode()).hexdigest()
    if(hash[0]=="0" and hash[1]=="0"and hash[2]=="0"and hash[3]=="0"and hash[4]=="0"):
        correctHash=True
    i+=1
print(f"Number needed for 5 0's at the start: {i}")
correctHash=False
i=0
while(not correctHash):
    string=input + str(i)
    hash = hashlib.md5(string.encode()).hexdigest()
    if(hash[0]=="0" and hash[1]=="0"and hash[2]=="0"and hash[3]=="0"and hash[4]=="0"and hash[5]=="0"):
        correctHash=True
    i+=1
print(f"Number needed for 6 0's at the start: {i}")