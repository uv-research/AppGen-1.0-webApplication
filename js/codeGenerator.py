import os
import sys
import shutil
import zipfile
import urllib

from js.htmlTemp import *
from js.jsTemp import *

endPath = "./finalApp"

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
        for dir in dirs:
            ziph.write(os.path.join(root, dir))

def initJsCodeCreater(c, o, self):
    checkDir(c, o, self)

def checkDir(c, o, self):
    try:
        shutil.rmtree(endPath)
    except OSError:
        createFiles(c, o, self)
    else:
        createFiles(c, o, self)    

def createFiles(c, o, self):
    try:
        os.makedirs(endPath)
        a = open("./finalApp/index.html","w+")
        a.write(base)
        a.close()
        b = open("./finalApp/script.js","w+")
        b.close()

    except OSError:
        self.sendMessage("""dir %s creation failed""" % endPath)
    else:
        self.sendMessage("""the dir %s is created successfully""" %endPath)
        generate(c, o, self)

def generate(count, operation, self):
    if count:
        self.sendMessage("""processing""")
        for d in range(0, count):
            writeInput(d)
        writeSubmit()
        writeInit()
        writeSubmitFunction(count, operation)
        self.sendMessage("""App successfully Created """)
        try:
            shutil.rmtree('./final.zip')
        except OSError:
            zipf = zipfile.ZipFile('final.zip', 'w', zipfile.ZIP_DEFLATED)
            zipdir(endPath, zipf)
            zipf.close()
            self.sendMessage("""App zipped successfully""")
        else:
            zipf = zipfile.ZipFile('final.zip', 'w', zipfile.ZIP_DEFLATED)
            zipdir(endPath, zipf)
            zipf.close() 
            self.sendMessage("""App zipped successfully""")        
