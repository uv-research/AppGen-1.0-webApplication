from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

def setup():
    chatbot = ChatBot('Bot')
    trainer = ChatterBotCorpusTrainer(chatbot)
    
    for file in os.listdir('./data/'):
        trainer.train('./data/'+file)
    
setup()