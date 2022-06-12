string = open('DP2_normal_link.txt').readlines()
res=''
for i in string:
    if not i.isspace():
        res=res+i.replace('\n', '')+"\n"

text_file = open("DP2_normal_link.txt", "w",encoding='utf-8')
text_file.write(res)
text_file.close()
