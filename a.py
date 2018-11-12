#!/usr/bin/python

class aPattern:
    def __init__(self, inString):
        self.value = inString 
        #self.components = ["one", "two", "three"] 
        self.components = [] 

class dList:
    def __init__(self, inFile):
        self.wordFile = open(inFile, "r")
        self.wordList = []
        for line in self.wordFile:
            line = line.rstrip('\n')
            #print line
            self.wordList.append(line)

if __name__ == '__main__':

    #print "begin"

    #a = aPattern("onetwothree")
    a = aPattern("one two three")
    #d = dList("infile.txt")
    d = dList("/usr/share/dict/words")
    print(a.value)
    #print(a.components)
    #print(d.wordList)
    for word in d.wordList:
        if a.value.find(word) != -1:
            print word
            a.components.append(word)
    print(a.components)
    #print "end"
