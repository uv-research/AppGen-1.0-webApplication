import os
import sys
import shutil
import zipfile

from vuejs.AppVue import *
from vuejs.babelConfig import *
from vuejs.baseComponent import *
from vuejs.indexHtml import *
from vuejs.mainJs import *
from vuejs.packageJson import *
from vuejs.README import *

endPath = "./finalApp"

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
        for dir in dirs:
            ziph.write(os.path.join(root, dir))

def initVuejsCodeCreater(c, o, self):
    checkDir(c, o, self)

def checkDir(c, o, self):
    try:
        shutil.rmtree(endPath)
    except OSError:
        createFiles(c, o, self)
    else:
        createFiles(c, o, self)

def createFiles(z, x, self):
    try:
        os.makedirs(endPath)
        os.makedirs("./finalApp/public")
        os.makedirs("./finalApp/src")
        os.makedirs("./finalApp/src/assets")
        os.makedirs("./finalApp/src/components")
        a = open("./finalApp/package.json","w+")
        a.write(package)
        a.close()
        b = open("./finalApp/README.md","w+")
        b.write(readme)
        b.close()
        c = open("./finalApp/babel.config.js","w+")
        c.write(bable)
        c.close()
        d = open("./finalApp/public/index.html","w+")
        d.write(indexhtml)
        d.close()
        e = open("./finalApp/src/App.vue","w+")
        e.write(appvue)
        e.close()
        f = open("./finalApp/src/main.js","w+")
        f.write(main)
        f.close()
        g = open("./finalApp/src/components/HelloWorld.vue","w+")
        g.close()

    except OSError:
        self.sendMessage("""dir %s creation failed""" % endPath)
    else:
        self.sendMessage("""the dir %s is created successfully""" %endPath)
        generate(z, x, self)

def generate(count, operation, self):
    if count:
        self.sendMessage("""processing""")
        writePart1()
        for d in range(0, count):
            writeInputs(d)
        writePart2()
        for e in range(0, count):
            writeInData(e)
        writePart3()
        if operation == "add":
            writeAddOperation(count)
        elif operation == "addition":
            writeAddOperation(count)
        elif operation == "sum":
            writeAddOperation(count)
        elif operation == "difference":
            writeSubOperation(count)
        elif operation == "subtract":
            writeSubOperation(count)
        elif operation == "subtraction":
            writeSubOperation(count)
        writePart4()
        self.sendMessage("""App successfully Created """)
        try:
            shutil.rmtree('./final.zip')
        except OSError:
            zipf = zipfile.ZipFile('final.zip', 'w', zipfile.ZIP_DEFLATED)
            zipdir(endPath, zipf)
            zipf.close()
            self.sendMessage("""App zipped successfully """)
        else:
            zipf = zipfile.ZipFile('final.zip', 'w', zipfile.ZIP_DEFLATED)
            zipdir(endPath, zipf)
            zipf.close() 
            self.sendMessage("""App zipped successfully""")
