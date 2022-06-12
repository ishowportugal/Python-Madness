import fileManager
tree=[]
class WebApp:
    def __init__(self, file):
        self.file=file
    def setDoctype(self,doctype):
        tree.insert(0,{"type":f"!doctype {doctype}","classes":None,"id":None,"close":False})
    def create(self):
        fileManager.create(self.file)
        fileobj=open(self.file, "w+")
        for element in tree:
            finalstring=f"<{element['type']}"
            if element["classes"]:
                classes="\""
                for i in element["classes"]:
                    classes+=i+" "
                finalstring+=" class="+classes[:-1]+"\""
            if element["id"]!=None:
                finalstring+=f" id=\"{element['id']}\""
            fileobj.write(finalstring+">")
            if element["close"]:
                if element["content"]:
                    fileobj.write("\n\t"+element["content"])
                fileobj.write("\n"+f"</{element['type']}>")
            fileobj.write("\n")
        fileobj.close()
    def addelement(self, type, content=None,classes=None,id=None,close=True):
        tree.append({
            "type": type,
            "content": content,
            "classes": classes,
            "id": id,
            "close": close
        })
    def settitle(self,title):
        tree.insert(0,{
            "type": "title",
            "content": title,
            "classes": None,
            "id": None,
            "close": True
        })
