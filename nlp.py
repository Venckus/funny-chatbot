#!/usr/local/bin/python3
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields
from datetime import datetime
import json, random

@dataclass(order=True, frozen=True)
class History:
    time: str = field() # datetime.now()
    sender: str = field()
    message: str = field() # default_factory=list, compare=True)

    # def update(self, message):
    #     self.message.append((message, datetime.now()))

@dataclass(order=True, frozen=True)
class Answer:
    keyword: str = field()
    response: str = field()

@dataclass(order=True, frozen=True)
class Context:
    keyword: list = field()
    text: list = field() # default_factory=list, compare=False)

class Nlp(object):
    'process messages'
    def __init__(self):
        self.history = []
        self.context = []
        self.context_lib = {
            "hello": [
                "hi",
                "hello",
                "hey",
                "greetings",
                "good morning",
                "good afternoon",
                "good night",
                "aloha"
            ],
            "bye": [
                "bye",
                "cya",
                "see ya",
                "exit"
            ],
            "cry": ["!"],
            "question": ["?"]
            # "!": "cry",
            # "?": "question"
        }
        self.answers = {}
        self.noise = ['o', 'a', 'the', '.', ',', '?', '!', ';']
        self.load_answers()
        # self.load_context()
    
    def process(self, sender, message):
        'process message and send response'
        self.proc_context(message)
        self.insert_update(sender, message)

        return self.proc_answer()

    def insert_update(self, sender, message):
        'update message history'
        
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if self.history == None:
            self.history = History(now, sender, message)
        else:
            self.history.append(History(now, sender, message))

    def proc_context(self, message):
        'analize to understand message type and context'

        for k, list in self.context_lib.items():
            for context in list:
                if context in message:
                    
                    self.context.append(k)
                    return
        else:
            self.context.append('neutral')

    def proc_answer(self):
        'find answer using context'

        # latest message string split to list
        msg = self.filter_noise(self.history[-1].message)

        # msg = self.history[-1].message
        if 'question' in self.context[-1]:
            # random reorder message words
            answer = f"{self.answers['question']}{self.set_random(msg)}."

        elif 'cry' in self.context[-1]:
            # appologise and ask what happend
            answer = f"{self.answers['disapointed']}."

        elif 'hello' in self.context[-1]:
            # say hi
            answer = f"{self.answers['hello']} :)"
        
        elif 'bye' in self.context[-1]:
            # say bye
            answer = f"{self.answers['bye']} :)"
        
        elif 'neutral' in self.context[-1]:
            # random reorder message words
            # answer = f"{self.answers['joint']}{self.set_random(msg)}."
            neutral = random.sample(self.answers['neutral'], 2)
            complex = neutral + msg
            answer = self.set_random(complex)

        else:
            # say i cant understand
            answer = self.answers['unknown']
        
        return answer

    def set_random(self, msg):
        # filtered = self.filter_noise(msg)
        return " ".join(random.sample(msg, len(msg)))

    def filter_noise(self, message):
        'split message into list & filter out noise'
        no_characters = message.translate(
            {ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        splited = no_characters.split()
        # filtered = [x for x in splited if x not in self.noise]
        return splited
    
    # def load_context(self):
    #     'read context.json to nlp context ojbect dict'
    #     with open('context.json') as json_file:
    #         f =json.load(json_file)
    #         for k, context in f.items():
    #             self.context_lib.append(Context(k, context))

    def load_answers(self):
        'read answers.json to dict'
        with open('answers.json') as json_file:
            f = json.load(json_file)
            for k, answer in f.items():
                # self.answers.append(Answer(k, answer))
                self.answers.update({k: answer})


# nlp = Nlp()
# nlp.insert_update('me', 'hello wa po ioi i')
# print(nlp.filter_noise('hello wa, a po ioi the i'))
# print(nlp.context_lib)
# print(nlp.filter_noise('wa ta fa?'))
# print('robot say:', nlp.process('me', 'hello'))
# print('robot say:', nlp.process('me', 'wa ta fa'))
