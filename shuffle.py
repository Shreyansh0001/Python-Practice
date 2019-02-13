import string
import random

def scramble(un):
    if(len(un)>3):
        foot = list(un[1:-1])
        random.shuffle(foot)
        str1 = un[0]+''.join(foot)+un[-1]+" "
    else:
        str1 = un+" "
    return str1
    
filename=input("enter the file name:")
with open(filename, 'r') as f:
   data = f.readlines()
file = open('testfile.txt','w')
str1=''
for line in data:
    sentences = line.split()
    for i in range(0,len(line.split())):
        str2 = scramble(sentences[i])
        str1 +=  ''.join(str2)
    str1+='\n'

file.write(str1)
file.close()
print("file has been scrambled")
 
