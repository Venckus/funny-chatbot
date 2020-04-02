#!/usr/local/bin/python3
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields
from datetime import datetime
import api
import filters
import json
import random


@dataclass(order=True, frozen=True)
class History:
    time: str = field()
    sender: str = field()
    message: str = field()


@dataclass(order=True, frozen=True)
class Answer:
    keyword: str = field()
    response: str = field()


@dataclass(order=True, frozen=True)
class Context:
    keyword: list = field()
    text: list = field()


class NLP(object):
    'natural language processing class'

    def __init__(self):
        self.history = []
        self.context = []
        self.load_templates()

    def process(self, sender, message):
        'process message and send response'

        self.proc_context(message)

        # update message history for later processing
        self.insert_update(sender, message)

        # check for API requests first
        response = self.check_api(message)

        if response != False:

            return response

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

            neutral = random.sample(self.answers['neutral'], 2)
            complex = neutral + msg
            answer = self.set_random(complex)

        else:
            # say i cant understand
            answer = self.answers['unknown']

        return answer

    def check_api(self, msg):
        'check message for api requests, return data if found any'

        api_list = self.context_lib['api']

        location = [l.lower() for l in msg.split()]

        for key in api_list:

            if all(a in msg for a in key):

                filtered = [f for f in location if f not in key]

                return self.proc_api(key, filtered)

        else:
            return False

    def proc_api(self, api_type, filtered):
        'process user request'

        if api_type == 'weather':

            # get city id from api
            city = self.detect_location(filtered)

            url = api.build_url(self.api_list[api_type], city)

            response = api.api_get(url)

            if response == False:

                return response

            else:
                return filters.weather(response)
        else:
            # proc joke for now
            joke = api.api_get(self.api_list[api_type]['url'])
            response = joke['value']
        return response

    def detect_location(self, location):
        'it could be new module for detection needed'

        list = self.load_file('locations')
        cities = list['list']

        for city in cities:

            if city['code'] in location:

                return city['code']

        else:
            # for default city use vilnius when match not found
            return 'vilnius'

    def set_random(self, msg):
        'randomise prepared answer before sending back to user'

        return " ".join(random.sample(msg, len(msg)))

    def filter_noise(self, message):
        'split message into list & filter out noise'

        no_characters = message.translate(
            {ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})

        splited = no_characters.split()

        return splited

    def load_templates(self):
        'load answers, context, api_list'

        self.answers = self.load_file('answers')
        self.context_lib = self.load_file('context_lib')
        self.api_list = self.load_file('api_list')

    def load_file(self, arg):  # name, attr
        'read .json files by name to attributes'

        fname = f'{arg}.json'
        result = {}

        with open(fname) as json_file:
            f = json.load(json_file)
            for k, answer in f.items():
                result.update({k: answer})
        return result


nlp = NLP()
print(nlp.process('me', 'joke tell'))
# nlp.insert_update('me', 'hello wa po ioi i')
# print(nlp.filter_noise('hello wa, a po ioi the i'))
# print('context LIB: ', nlp.context_lib['api'])
# print('answers: ', nlp.answers)
# print(nlp.filter_noise('wa ta fa?'))
# print('robot say:', nlp.process('me', 'hello'))
# print('robot say:', nlp.process('me', 'wa ta fa'))
