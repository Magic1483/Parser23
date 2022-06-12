import string
from unicodedata import name
from webbrowser import get


with open('DP2.txt','r',encoding='utf-8') as f:
    contents = f.read()

s1=str(contents)
arr1=[]
arr1=s1.split("[")


global nameList
nameList=''
def getInf(val):
    tmp=[]
    tmp=str(val).split("\n")
    
    print("Name:    "+str(tmp[1]))
    global nameList
    nameList=nameList+str(tmp[1])+"\n"
            

for i in range(len(arr1)):
    getInf(arr1[i])
    
text_file = open("DP2_names.txt", "w")
text_file.write(nameList)
text_file.close()


global Links
Links=''
def getLink():
    Lcount=0
    for p in arr1:
        if  "aHR0c" in p:
            Lcount=Lcount+1
            global Links
            Links=Links+p+"\n"
            #print(p)
    print(Lcount)







