#!/usr/bin/python

class aPattern:
    def __init__(self, inString):
        self.value = inString
        self.wordDict = {}
        self.wordDict[self.value] = {}
        #self.components = ["one", "two", "three"] 
        self.components = list(inString) 
        for c in set(self.components):
            self.wordDict[self.value][c] = self.components.count(c)

class dList:
    def __init__(self, inFile):
        self.wordFile = open(inFile, "r")
#        self.wordList = []
        self.wordDict = {}
        for line in self.wordFile:
            line = line.rstrip('\n')
            #print line
            self.wordDict[line] = {}
            lineChars = list(line) 
            for c in set(lineChars):
                #self.wordDict[line] = [ c : self.wordDict[line][c]++ ]
                self.wordDict[line][c] = lineChars.count(c)
###            if (line == "disillusioned"):
###                print line, self.wordDict[line]
##        print "disillusioned", self.wordDict['disillusioned']
        self.wordFile.close

if __name__ == '__main__':

    #print "begin"

    #a = aPattern("onetwothree")
    #a = aPattern("one two three")
    #i = aPattern("gel leg")
    #i = aPattern("gel")
    #i = aPattern("admirer")
    #i = aPattern("deductions")
    i = aPattern("listen")
    #d = dList("infile.txt")
    d = dList("/usr/share/dict/words")
    #print(i.value)
    #print(i.components)
    #print(d.wordList)
###    for word in d.wordDict.keys():
#        w = aPattern(word)
###         print d.wordDict[ word ]
###         wordChars = list(word)
    #print "disillusioned[d]", d.wordDict['disillusioned']['d']
    #print "disillusioned[i]", d.wordDict['disillusioned']['i']
    #print "disillusioned[s]", d.wordDict['disillusioned']['s']
    #print "disillusioned[l]", d.wordDict['disillusioned']['l']
    #print "disillusioned", d.wordDict['disillusioned']
    #print "illusioned", d.wordDict['illusioned']
    #print "gel", d.wordDict['gel']
    #print "gel", i.wordDict['gel']
    #print "leg", d.wordDict['leg']
    #print "dad", d.wordDict['dad']
    #print "add", d.wordDict['add']
#        a = i
#        for c in w.components:
            #print w.value
            #print w.components
            #print a.value
            #print c
#            if a.components.count(c) > 0:
#                a.components.remove(c)
#                w.components.remove(c)
#                print a.components
    #print(a.components)
    #print "end"
            
    print i.value
    print i.wordDict[i.value]
    for word in d.wordDict.keys():
        #print word
        if(len(word) == len(i.value) and word != i.value):
            if(d.wordDict[word] == i.wordDict[i.value]):
                print word
                print d.wordDict[word]
            #print d.wordDict[word]
