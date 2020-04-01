#!/usr/local/bin/python3
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields
from datetime import datetime
import api_list
import json
import random


@dataclass(order=True, frozen=True)
class History:
    time: str = field()  # datetime.now()
    sender: str = field()
    message: str = field()  # default_factory=list, compare=True)

    # def update(self, message):
    #     self.message.append((message, datetime.now()))


@dataclass(order=True, frozen=True)
class Answer:
    keyword: str = field()
    response: str = field()


@dataclass(order=True, frozen=True)
class Context:
    keyword: list = field()
    text: list = field()  # default_factory=list, compare=False)


class NLP(object):
    'process messages'

    def __init__(self):
        self.history = []
        self.context = []
        self.context_lib = {}
        self.api_list = []
        self.answers = {}
        self.load_parameters()

    def process(self, sender, message):
        'process message and send response'
        self.proc_context(message)
        self.insert_update(sender, message)

        return self.find_answer()

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

    def find_answer(self):
        'find answer'

        # latest message string split to list
        msg = self.filter_noise(self.history[-1].message)

        for k, answer in self.answers.items():
            if k in msg:
                return self.proc_answer(k, answer, msg)

    def proc_answer(self, type, answer, msg):
        'decide how handle the response'

        if type in ['hello', 'bye']:
            # say hi or bye
            answer = f"{answer} :)"

        elif type == 'question':
            # random reorder message words
            answer = f"{answer}{self.set_random(msg)}."

        elif type == 'cry':
            # appologise and ask what happend
            answer = f"{answer}."

        elif type == 'api':
            self.api.exec(answer)

        elif type == 'neutral':
            # random reorder message words
            # answer = f"{self.answers['joint']}{self.set_random(msg)}."
            neutral = random.sample(answer, 2)
            complex = neutral + msg
            answer = self.set_random(complex)

        # else:
        #     answer = self.answers['unknown']

        return answer

    def set_random(self, msg):
        # filtered = self.filter_noise(msg)
        return " ".join(random.sample(msg, len(msg)))

    def filter_noise(self, message):
        'split message into list & filter out noise'
        no_characters = message.translate(
            {ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        splited = no_characters.split()
        return splited

    def load_file(self, filename, param):
        'read files'
        fname = filename + '.json'
        with open(fname) as json_file:
            f = json.load(json_file)
            for k, val in f.items():
                param.update({k: val})

    def load_parameters(self):
        'load all needed parameters from files'
        self.load_file('answers', self.answers)
        self.load_file('context', self.context_lib)

    def load_answers(self):
        'read answers.json to dict'
        with open('answers.json') as json_file:
            f = json.load(json_file)
            for k, answer in f.items():
                # self.answers.append(Answer(k, answer))
                self.answers.update({k: answer})

    def prepare_api(self):
        'prepare api requests'
        for k, api in self.api_list:
            self.apis[k] = {''.join(x for x in api)}


# nlp = NLP()
# nlp.insert_update('me', 'hello wa po ioi i')
# print(nlp.filter_noise('hello wa, a po ioi the i'))
# print(nlp.context_lib)
# print(nlp.filter_noise('wa ta fa?'))
# print('robot say:', nlp.process('me', 'hello'))
# print('robot say:', nlp.process('me', 'wa ta fa'))
