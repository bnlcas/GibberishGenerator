# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:58:15 2017

@author: Ben Lucas
"""

import random


#s = "all the queens horses and all the king's men couldnt put it 
GibberishWordBank = GenGibberishWordBank(s)
#GenGibberishSample(GibberishWordBank, 'asw', 200)
targLen = 3
sampleLen = 200
targ = GenGibberishTarg(GibberishWordBank, targLen)
print(targ)
GenGibberishSample(GibberishWordBank, targ, sampleLen)

nSamples = 100
WriteGibberishTxt(GibberishWordBank,sampleLen, targLen, nSamples)


def WriteGibberishTxt(GibberishWords, sampleLen, targLen, nSamples):
    filename = 'C:/Users/Ben Lucas/Documents/textLegibility/Gibberish2/GibberishSamples_' + str(sampleLen) + '_' + str(targLen) + '.txt'
    f = open(filename, 'w')
    for i in range(nSamples):
        targ = GenGibberishTarg(GibberishWords, targLen)
        f.write(targ + '\n')
        samp = GenGibberishSample(GibberishWordBank, targ, sampleLen)
        f.write(samp + '\n')
    f.close()


def GenGibberishWordBank(s):
    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','ch', 'sh', 'th','sp', 'wh']
    punctuation = ['.',',',' ',"'", '?','!']
    chars = list(s.lower())

    consonants_s = [x for x in chars if x in consonants]
    for i in range(len(chars)-1):
        if ''.join([chars[i], chars[i+1]]) in consonants:
            consonants_s.append(''.join([chars[i], chars[i+1]]))

    vowels_s = [x for x in chars if x in vowels]

    gibberish_chars = []
    for x in chars:
        if(x=='.' or x == ' ' or x==','):
            gibberish_chars.append(x)
        elif(x in vowels):
            gibberish_chars.append(random.choice(vowels_s))
        elif(x in consonants):
            gibberish_chars.append(random.choice(consonants_s))

    outString = ''.join(gibberish_chars)

    GibberishWordBank = outString.split(' ')

    MinWordSize = 4
    MaxWordSize = 8

    GibberishWordBank = [x for x in GibberishWordBank if len(x) >= MinWordSize and len(x) <= MaxWordSize]
    return GibberishWordBank



def GenGibberishTarg(GibberishBank, nChars):
    word = ''
    while (len(word) < nChars):
        word = random.sample(GibberishBank,1)[0]
    target = word[0:(nChars)]
    return target



# Generate Gibberish Samples from a word bank (Gibberish) includes a target
# sequence of characters
# Defaults: 5 insertions of the target, min separation of 2 characters between target elements
def GenGibberishSample(Gibberish, target, nChars):
    minWordSize = 4
    minSep = 20 # minimum number of characters separting sequence
    nInstances = 5 # Number of instances 
    nWords = nChars*8
    GibSample = list(" ".join(random.sample(Gibberish, nWords))) # ordered list of word characters
    GibSample = GibSample[0:(nChars)]
    
    # CLip the Tail:
    GibSample = ClipTail(GibSample, "a"*minWordSize)

    # Wipe any chance occurances of the target sequence from the sample
    GibSample = CleanSample(GibSample, target)
    
    InsertionInds = GetVialbeInsertionInds(GibSample, target)
    GibSample = InsertTarget(GibSample, target, InsertionInds, nInstances, minSep)
    # One more scrub:
    if CountInstances(GibSample, target) != nInstances:
        print("WARNING WRONG NUMBER OF TARGETS FOUND")
        return GenGibberishSample(Gibberish, target, nChars) # Bad Idea
    else:
        return "".join(GibSample)


def CleanSample(sample, targ):
        containsTarget = True
        nLoops = 0
        while containsTarget:
            nTargs = 0
            for i in range(len(sample)-len(targ)):
                seq = "".join(sample[i:(i+len(targ))])
                if seq == targ:
                    sample[i] = random.choice(['a','e','i','o','u', 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v'])
                    nTargs += 1
            if nTargs == 0:
                containsTarget = False
            nLoops += 1
            if nLoops == 100:
                containsTarget = False
                print("SAMPLE SCRUB FAILURE")
        return sample
                
def ClipTail(GibSample, target):
    nChars = len(target)
    
    if " " in GibSample[-nChars:]:
        tail = []
        for x in GibSample[-nChars:]:
            if x == " ":
                break
            else:
                tail.append(x)
        GibSample = GibSample[:(-nChars)] + tail
    return GibSample


## Assemble a list of viable insertion indecies
def GetVialbeInsertionInds(GibSample, target):
    ViableInsertions = []
    for k in range(len(GibSample)-len(target)):
        if " " not in GibSample[k:(k+len(target))]:
            ViableInsertions.append(k)
    return ViableInsertions


def InsertTarget(GibSample, target, InsertionInds, nInstances, minSep):
    indsNotSpaced = True
    while indsNotSpaced:
        inserts = sorted(random.sample(InsertionInds, nInstances))
        x = inserts[1:]
        y = inserts[:-1]
        diffs = [x[i] - y[i] for i in range(len(x))]
        indsNotSpaced = (len([k for k in diffs if k >= minSep]) != len(diffs))
    for x in inserts:
        GibSample[x:(x+len(target))] = list(target)
    return GibSample
                

def CountInstances(sample, targ):
    nTargs = 0
    for i in range(len(sample) - len(targ)):
        seq = "".join(sample[i:(i+len(targ))])
        if seq == targ:
            nTargs += 1
    return nTargs
    