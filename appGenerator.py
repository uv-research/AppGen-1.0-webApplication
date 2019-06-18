import os
import sys
from js.codeGenerator import initJsCodeCreater
from vuejs.codeGenerator import initVuejsCodeCreater
from angular.codeGenerator import initAngularCodeCreater

endPath = "./finalApp"

class codekey:
    operation = ''
    count = ''
    language = ''

key = codekey()

operationList = ['add','addition','sum','difference','subtract','subtraction']

language = ['js','javascript','vuejs','reactjs','angular']

def startGenerator(inputData, self):
    key.count = ''
    key.operation = ''
    key.language = ''
    splitData = inputData.split(" ")
    identifyKeyWords(splitData, self)

def identifyKeyWords(data, self):
    for a in data:
        try:
            val = int(a)
            key.count = val
        except ValueError:
            if a == data:
                print('no count') 
        
        for b in operationList:
            if a == b:
                key.operation = a
        
        for c in language:
            if a == c:
                key.language = a
    onStackIdentification(self)

def onStackIdentification(self):
    if key.language == 'javascript':
        self.sendMessage("""Bot started coding in javascript""")
        initJsCodeCreater(key.count, key.operation, self)

    elif key.language == 'vuejs':
        self.sendMessage("""Bot started coding in vuejs""")
        initVuejsCodeCreater(key.count, key.operation, self)
    
    elif key.language == 'angular':
        self.sendMessage("""Bot started coding in angular""")
        initAngularCodeCreater(key.count, key.operation, self)
    
    else:
        self.sendMessage("""sorry! The bot is not yet trained to create app in this language. will train it as soon as possible.""")

