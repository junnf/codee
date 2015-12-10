#!/usr/bin/env python
from __future__ import division
import re
import math

def getwords(doc):
    spl = re.compile('\\W*')
    words = spl.split(doc)
    #word filter
    return dict([(x.lower(),1) for x in words if len(x)>2 and len(x)<15])

class Classifier(object):
    def __init__(self, getfeatures, filename = None):
        self.fc = {}
        self.cc = {}
        self.getfeatures = getfeatures
    
    def incf(self, f, cat):
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat, 0)
        self.fc[f][cat]+=1

    def incc(self, cat):
        self.cc.setdefault(cat, 0)
        self.cc[cat]+=1

    def fcount(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0
    
    def catcount(self, cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0.0

    def totalcount(self):
        return sum(self.cc.values())

    def categories(self):
        return self.cc.keys()

    def train(self, item, cat):
        features = self.getfeatures(item)
        for f in features:
            self.incf(f,cat)
        self.incc(cat)

    # get P(x|y)
    def fprob(self, f, cat):
        if self.catcount(cat) == 0:
            return 0
        return (self.fcount(f, cat) / self.catcount(cat))

    def weightedprob(self, f, cat, prf, weight=1.0, ap=0.5):
        basicprob=prf(f,cat)
        totals = sum([self.fcount(f,c) for c in self.categories()])
        bp=((weight*ap)+(totals*basicprob))/(weight+totals)
        return bp

class bayes(Classifier):
    def docprob(self, item, cat):
        features = self.getfeatures(item)
        p = 1
        for f in features:
            p *= self.weightedprob(f,cat,self.fprob)
        return p

    def prob(self, item, cat):
        catprob = self.catcount(cat)/self.totalcount()
        docprob = self.docprob(item,cat)
        return docprob*catprob


if __name__ == '__main__':
    cla = bayes(getwords)
    f1 = open('_dataset_')
    f2 = open('_dataset_2')
    for x in f1:
        cla.train(x,'bad')
    for y in f2:
        cla.train(y,'good')
    print cla.fcount('brave','good')
    print cla.weightedprob('brave','good',cla.fprob)
    print cla.prob('kind is good nature', 'good')
    print cla.prob('kind is good nature', 'bad')


