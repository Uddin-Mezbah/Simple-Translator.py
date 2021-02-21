import os
from tabulate import tabulate
from googletrans import Translator

class Translator():
    def __init__(self,word,language):
        self.word = word
        self.language = language
        self.Translator = Translator()

    def translator(self):
        translator = self.translator(self.word,dest=self.language)
        data = [["Original Sentence: ", "Translated Sentence"],
                [self.word. str(translator.text)]]
        return tabulate(data,headers="firstrow",tablefmt="fancy_grid")

    def __str__(self):
        return self.translator()

if __name__ == '__main__':
    sentence = input("Enter string to translate >> ")
    os.system("cls")
    print(Translator(sentence,"en"))


