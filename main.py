import re
import string


def removePunc(text):
    table = string.maketrans("","")
    return text.translate(table, string.punctuation)

stopwords = ["the", "a", "I", "<p>", "</p>"]
stopwordPattern = re.compile(r"\b(" + r"|".join(stopwords) + ")\b")
def removeStopwords(text):
    return re.replace(stopwordPattern,"". text)

def tokenize(documentText):
    text = removeStopwords(removePunc(documentText))
    return text.split()


def processData(file):
    pass
