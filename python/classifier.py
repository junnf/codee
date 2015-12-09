#!/usr/bin/env python
import re
import math

def getwords(doc):
    spl = re.compile('\\W*')
    words = spl.split(doc)
    return dict([(x,1) for x in words if len(x)>2 and len(x)<20])

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
        return 0,0
    
    def catcount(self, cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0

    def totalcount(self):
        return sum(self.cc.values())

    def categor(self):
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
        else:
            return self.fcount(f, cat)/self.catcount(cat)

    def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
        basicprob=prf(f,cat)
        totals=sum([self.fcount(f,c) for c in self.categories()])
        bp=((weight*ap)+(totals*basicprob))/(weight+totals)
        return bp


if __name__ == '__main__':
    cl = Classifier(getwords)
    cl.train('hello, everyone i want you', 'good')
    cl.train('hello, everyone i want fuck you', 'bad')
    cl.train('fuck you get out!','bad')
    print 'fc'
    print cl.fc 
    print '\n'
    print 'cc'
    print cl.cc
    

