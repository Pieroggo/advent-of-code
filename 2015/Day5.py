file=open("inputDay5.txt","r")
input=file.read()
strings=input.split("\n")
#part 1
vowels=["a","e","i","o","u"]
naughtySubstrings=["ab","cd","pq","xy"]
goodStrings=0
for string in strings:
    hasRepeatedChar=False
    hasNaughtySubstring=False
    vowelCounter=0
    for i in range(len(string)-1):
        if(vowels.count(string[i])!=0):
            vowelCounter+=1
        if(string[i]==string[i+1]):
            hasRepeatedChar=True
        if(naughtySubstrings.count(string[i]+string[i+1])!=0):
            hasNaughtySubstring=True
    if(vowels.count(string[-1])!=0):
        vowelCounter+=1
    if(vowelCounter>=3 and hasRepeatedChar and not hasNaughtySubstring):
        goodStrings+=1
print(f'Good strings: {goodStrings}')
#part 2
goodStrings=0
for string in strings:
    partRepeat=False
    mirrorPart=False
    for i in range(len(string)-2):
        j=i+2
        while(j<len(string)-1):
            if(string[i]+string[i+1]==string[j]+string[j+1]):
                partRepeat=True
            j+=1
        if(string[i]==string[i+2]):
            mirrorPart=True
    if(mirrorPart and partRepeat):
        goodStrings+=1
print(f'Even better strings: {goodStrings}')