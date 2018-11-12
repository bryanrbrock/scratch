#!/usr/bin/python

class aPattern:
    def __init__(self, inString):
        self.value = inString
        #self.components = ["one", "two", "three"] 
        self.components = list(inString) 

class dList:
    def __init__(self, inFile):
        self.wordFile = open(inFile, "r")
        self.wordList = []
        for line in self.wordFile:
            line = line.rstrip('\n')
            #print line
            self.wordList.append(line)
        self.wordFile.close

if __name__ == '__main__':

    #print "begin"

    #a = aPattern("onetwothree")
    #a = aPattern("one two three")
    a = aPattern("gel leg")
    #d = dList("infile.txt")
    d = dList("/usr/share/dict/words")
    print(a.value)
    print(a.components)
    #print(d.wordList)
    for word in d.wordList:
        w = aPattern(word)
        if a.value.find(w.value) != -1:
            print w.value
            a.components.append(w.value)
    print(a.components)
    #print "end"
