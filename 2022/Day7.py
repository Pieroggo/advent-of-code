def sizeOfDir(dir:'Folder'):
    sum=0
    if(dir.children is None):
        return 0
    for child in dir.children:
        if type(child) is File:
            sum+=child.size
        else:
            sum+=sizeOfDir(child)
    return sum
class File:
    name:str
    size:int
    parent:"Folder"
    def __init__(self,n:str,i:int,p:"Folder"=None):
        self.name=n
        self.size=i
        self.parent=p
    def __str__(self):
        return f"{self.name}:{self.size}"
    def __repr__(self):
        return f"{self.name}:{self.size}"
class Folder:
    name:str
    parent:'Folder'
    children:list=[]
    def __init__(self,n:str,p:'Folder'=None):
        self.name=n
        self.parent=p
        self.children=[]
    def attach_file(self,file:File):
        self.children+=[file]
    def attach_dir(self,folder:"Folder"):
        self.children+=[folder]
    def __repr__(self):
        string="["
        for child in self.children:
            string+=child.name+" ,"
        return self.name+": "+string+"]"
file=open("testDay7.txt","r")
contents=file.read().split("\n")
start=Folder("/",None)
file_list=[]
current_directory=start
creator_mode=True
for line in contents[1:]:
    parts=line.split(" ")
    if(parts[0]=="$"):
        if(parts[1]=="cd"):
            creator_mode=False
        if(parts[1]=="ls"):
            creator_mode=True
            continue
    if creator_mode:
        if(parts[0]=="dir"):
            current_directory.attach_dir(Folder(parts[1],current_directory))
        else:
            file=File(parts[1],int(parts[0]),current_directory)
            file_list+=[file]
            current_directory.attach_file(file)
    else:
        if(parts[2]==".."):
            current_directory=current_directory.parent
        else:
            print(parts[2])
            index=0
            for i,child in enumerate(current_directory.children):
                if(child.name==parts[2]):
                     index=i
            current_directory=current_directory.children[index]
    print(current_directory)
dirs_list={}
dirs_list["/"]=sizeOfDir(start)
#for file in file_list:
 #   current_parent=file.parent
  #  while(current_parent is not None):
   #     if current_parent.name in dirs_list:
    #        dirs_list[current_parent.name]+=file.size
     #   else:
      #      dirs_list[current_parent.name]=file.size
       # current_parent=current_parent.parent
print(dirs_list)
#Part 1
small_dirs_sum=0
for dir in dirs_list:
    if(dirs_list[dir]<100000):
        small_dirs_sum+=dirs_list[dir]
print(small_dirs_sum)

        