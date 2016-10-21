from xml.sax.handler import ContentHandler
import xml.sax
import xml.parsers.expat
import ConfigParser
import xml.sax
import random
import re


class Brain():
    def __init__(self):
        self.name = "Nao"


class AnsFinder(xml.sax.handler.ContentHandler, xml.sax.handler.ErrorHandler):
    def getWords(self, text):
        return re.compile('\w+').findall(text)

    def subtractLists(self, a, b):
        return a if len(b) == 0 else [a[:i] + self.subtractLists(a[i+1:], b[1:])
                                  for i in [a.index(b[0])]][0]

    def takeStar(self, with_star, longer):
        # print(with_star, longer)
        with_star = self.getWords(with_star)
        long = self.getWords(longer)

        return " ".join(self.subtractLists(long, with_star))


    def __init__(self, input_text, that):
        self.that = that
        self.input = input_text
        self.curpath = []
        self.isPattern = False
        self.isTemplate = False
        self.isContext = False
        self.isRandom = False
        self.isHere = False
        self.isSrai = False
        self.isStar = False
        self.ans = ""
        self.random_table = []

    def startElement(self, name, attrs):
        if name == "pattern":
            self.isPattern = True
        if name == "template" and self.isContext:
            self.isTemplate = True
        if name == "random" and self.isContext:
            self.isRandom = True
        if name == "srai" and self.isContext:
            self.isSrai = True
        if name == "star" and self.isContext:
            self.isStar = True

    def endElement(self, name):
        if name == "category":
            self.isPattern = False
            self.isContext = False
            self.isRandom = False

            self.random_table = []
        elif name == "random" and self.isContext:
            self.ans = random.choice(self.random_table)
            # print(self.random_table, "och")
        pass

    def characters(self, data):
        if self.isRandom:
            self.random_table.append(data)

        if self.isTemplate:
            self.ans = data
            self.isTemplate = False


        #OTOZ NIE DO KONCA!!!
        if self.isStar:
            self.ans += " " + data

        if self.isPattern:

            # data_to_compare = (''.join([c for c in "LOVE ME BY *" if c not in ('_', '* ', '*')]))
            #
            # data_to_compare = self.getWords(data_to_compare)
            # input_to_compare = self.getWords(self.input)
            # temp3 = [x for x in (input_to_compare) if x not in (data_to_compare)]
            # if not len(temp3) == len(data_to_compare):
            #     print(data)

            # print(''.join([c for c in data if c not in ('_', '*')]))
            # # if data == self.input:
            #
            if self.input.__contains__(''.join([c for c in data if c not in ('_', '*')])):
                if len(data) > 1:
                    self.isContext = True
                # print(self.input, data, "XXXX")
            # if len(data) > 1:
            #         self.isContext = True

class Interlocutor:
    def __init__(self):
        self.that = ""


    def give_ans(self, text_in):
        parser = xml.sax.make_parser()
        text_in = ((''.join([c for c in text_in if c not in (',', '.', '?', '!')]))).upper()
        handler = AnsFinder(text_in, self.that)
        parser.setContentHandler(handler)
        parser.parse(open('aiml_stu.aiml'))
        if handler.isSrai:
            new_text = handler.ans
            handler = AnsFinder(new_text, self.that)
            parser.setContentHandler(handler)
            parser.parse(open('aiml_stu.aiml'))

        self.that = handler.ans
        return handler.ans



def getWords(text):
    return re.compile('\w+').findall(text)

if __name__ == '__main__':
    intrlocu = Interlocutor()

    while(True):
        print(intrlocu.give_ans(raw_input("You:  ")))
