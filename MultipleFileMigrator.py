import os, shutil
#from os.path import join

dest = ['paths of the destination'];
src = "path of the source"
count = input("Enter the number of documents to be migrated")
file_name = []
i=0;
while i < int(count):
    file_name.append(input("Enter file name"))
    i+=1;
i=0;
while i < len(file_name):
   
    for root, dirs, files in os.walk("path of the source"):
        if file_name[i] in files:
            print ("Found")
            break;
        else:
            print('Try Again with correct file name')
            exit()
    full_path = os.path.join(src, file_name[i])
    t=0
    while t < len(dest):
        shutil.copy(full_path, dest[t])
        t+=1;   
    i+=1;

print ("Document Migrated Successfully")
exit()    