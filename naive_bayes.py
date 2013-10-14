from collections import defaultdict
from itertools import izip

class NaiveBayes(object):
    """Computes Naive Bayes Classifier for corpuse"""
    def __init__(self, arg):
        pass

    def train(self, documents, tags):

        def defaultDictFactory(factory):
            return lambda : defaultdict(factory)

        tagFreq = defaultdict(int)
        tagWordCondFreq = defaultdict(defaultDictFactory(int))
        self.nDocs = len(documents)

        for tags, document in izip(tags, documents):
            tags  = document.tags
            for tag in tags:
                tagFreq[tag] += 1

                # Right now, use a multvariate Bernoulli event model
                for word in set(self.getDocumentWords(document)):
                    tagWordCondFreq[tag][word] += 1


    def test(self, document):

        return tags