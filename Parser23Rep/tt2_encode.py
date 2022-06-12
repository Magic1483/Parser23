import base64
from email.mime import base
import string



with open('DP2_parse_link.txt','r',encoding='utf-8') as f:
    contents = f.read()

arr1=[]
arr1=str(contents).split("\n")
Errors=[]
errNumbers=[]

def EncodeBase64(val):
    try:
        base64_bytes = val.encode('utf-8')
        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes.decode('utf-8')
    except:
        Errors.append(val)
        return "undef"

strFINAL=''
undefCount=0
for i in range(len(arr1)):
    #print(EncodeBase64(str(arr1[i])))
    strFINAL=strFINAL+EncodeBase64(str(arr1[i]))+"\n"
    if(EncodeBase64(str(arr1[i]))=="undef"):
        undefCount=undefCount+1
        errNumbers.append(i)


strFINAL=strFINAL+"\nUndefined links:   "+str(undefCount)

text_file = open("DP2_normal_link.txt", "w")
text_file.write(strFINAL)
text_file.close()

print(errNumbers)

