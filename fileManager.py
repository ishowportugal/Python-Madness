import re
import os
import shutil
def exists(file):
    return os.path.exists(file)
def read(file):
    filee=open(file)
    content=re.findall("[^,]+",filee.read())
    filee.close()
    return content
def write(file,listValue):
    file=open(file,"w")
    file.write(repr(listValue).replace("[","").replace("]","").replace("'","").replace(", ",","))
    file.close()
def create(file):
    if not exists(file):
        open(file,"w").close()
def delete(file):
    if exists(file):
        os.remove(file)
def clear(file):
    fileObject=open(file,"w")
    fileObject.write("")
    fileObject.close()
def rename(file,newName):
    content=read(file)
    delete(file)
    create(newName)
    write(newName,content)
def encrypt(file):
    if os.path.exists(file):
        fileObject=open(file,"r+")
        contents=fileObject.read()
        encrypted=[]
        for i in contents:
            encrypted.append(str(ord(i)))
        fileObject.close()
        filee=open(file,"w")
        filee.write(repr(encrypted).replace("[","").replace("]","").replace("'","").replace(", ","|"))
        filee.close()
def decrypt(file):
    if os.path.exists(file):
        decrypted=""
        filee=open(file)
        content=re.findall("[^|]+",filee.read())
        filee.close()
        for i in content:
            decrypted+=chr(int(i))
        filee=open(file,"w")
        clear(file)
        filee.write(decrypted)
        filee.close()
def createFolder(folder):
    os.mkdir(folder)
def deleteFolder(folder):
    shutil.rmtree(folder)
