import os
import shutil

files = os.listdir('.')
file=[]

for x in files:
    if os.path.isdir(x):
        file.append(x)

print(file)

for i in file:
    source='./'+i
    img_list = os.listdir(source)
    for j in img_list:
        new_source=source+'/'+j
        x=new_source.split('/')
        new_x=x[0]+'/new'+'/'+x[1]+x[2]
        shutil.move(new_source,new_x)