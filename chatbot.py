from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from appGenerator import startGenerator
import datetime

def get_response(usrText, self):
    bot = ChatBot('Bot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.90,
            'default_response': 'I am sorry, but I do not understand.'
        },
        'chatterbot.logic.MathematicalEvaluation',
    ])
    trainer = ChatterBotCorpusTrainer(bot)

    while True:
        currentDT = datetime.datetime.now()
        if usrText.strip().lower().startswith( 'create' ):
            startGenerator(usrText.strip().lower(), self)
            return('')
        elif usrText.strip().lower() == 'bye':
            return('bye')
            break
        elif usrText.strip().lower() == 'time':
            return(currentDT.strftime("%I:%M %p"))
        elif usrText.strip().lower() == 'date':
            return(currentDT.strftime("%d/%m/%y"))
        elif usrText.strip().lower() == 'help':
            return("""use 'create' keyword to start creating app and also specify the language in which app should be developed.<br/>
            example: 'create addition of 2 numbers in vuejs'""")
        elif usrText.strip().lower() == 'list':
            return("""use params to list: <br/>
        '-O' for listing operations <br/>   
        '-L' for listing the languages in which bot can build app""")
        elif usrText.strip().lower() == 'list -o':
            return("""List of operations:<br/>
        'add / addition / sum'    <br/>
        'difference / subtract / subtraction'""")
        elif usrText.strip().lower() == 'list -l':
            return("""List of languages in which bot can build apps:<br/>
        'javascript'    <br/>
        'vuejs'           <br/>
        'angular'""")           
        else:
            result = bot.get_response(usrText.strip())
            reply = str(result)
            return(reply)

        
