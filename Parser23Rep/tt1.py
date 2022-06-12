#Channel: 📂Share Assets / 📂share-courses as DP1

#Channel: 📂Share Assets / 📂share-stuffs

with open('DP2.txt','r',encoding='utf-8') as f:
    contents = f.read()

s1=str(contents)
arr1=[]
arr1=s1.split("Coordinates:")
#print(arr1[4])
tmp1=[]

tmp1=arr1[5].split("{Embed}")


#print(range(len(arr1)))
#FINAL FUNC
global key4
key4=0
res=[]



strM=""

#print(len(arr1))
for z in range(len(arr1)):
    tmp=[]
    tmp=arr1[z].split("{Embed}")
    
    #res[z]=tmp[0]

    strM=strM+tmp[0]+"\n"

    #print(tmp[0])

#print(strM.split("\n"))

strD=[]
strD=strM.split("\n")


keyD=0
strD2=''
for p in strD:
    if "aHR0" in p:
        #print(p)
        strD2=strD2+p+"\n"
        keyD=keyD+1

#print(strD2)

text_file = open("DP2_parse_link.txt", "w")
text_file.write(strD2)
text_file.close()









