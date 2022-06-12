from tester import dotest
file=open("write.txt","r")
data=file.read()
file.close()
key=data[:2]
contents=data[2:]
dotest(data.isnumeric())
testkey=int(contents)%(len(contents)**2)%100
dotest(int(key)==int(testkey))
splitnumbers=[]
for i in range(0,len(contents),6):
    splitnumbers.append(contents[i:i+6])
final=""
for i in splitnumbers:
    individualkey=i[0]
    value=i[1:]
    total=0
    value=str(int(value)-int(individualkey))
    for i in value:
        total+=int(i)
    dotest(((total%5)+4)==int(individualkey))
    final+=chr(int(value[1:]))
print(final)

