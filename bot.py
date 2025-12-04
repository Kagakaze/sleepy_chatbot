#!/usr/bin/env python3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk

nltk.download('punkt_tab')

chatbot = ChatBot("Sleepy Yumi")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")