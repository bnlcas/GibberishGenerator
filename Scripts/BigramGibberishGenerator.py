# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:20:58 2017

@author: Ben Lucas
"""
# This file contains functions to create a data structure outlining the bigram transition probabilities for
# the characters found in a corpus of text
# to run this, load a corpus of text as a single string, and then run Main(corpus)
# Alternatively compile the functions and then enter the following lines in the console:
    # corpus = 'sample text...'
    # bigramStruct = GenerateBigramDictionary(corpus)
    # gibberishSample = GenerateGibberish(bigramStruct, 200)

from numpy import random as rand

def GenerateBigramDictionary(corpus):
    corpus = corpus.lower()
    chars = list(set(corpus.lower()))
    bigramsDict = {}
    for ch in chars:
        bigramsDict[ch] = GetBiGramDictChar(corpus, chars, ch)
    return bigramsDict

def GetBiGramDictChar(corpus, chars, ch):
    charInds = [i for (i, c) in enumerate(corpus) if c == ch and i < (len(corpus)-1)]
    charCount = 1.0 * len(charInds)
    charBigramDict = {}
    for c in chars:
        transitionInds = [i for i in charInds if (corpus[i+1] == c)]
        charBigramDict[c] = (1.0 * len(transitionInds)) / charCount
    return charBigramDict

def GetCharacterDistribution(corpus):
    chars = list(set(corpus.lower()))
    corpusSize = len(corpus)
    probs = [1.0*len([i for (i,c) in enumerate(corpus) if c == ch])/corpusSize for ch in chars]
    return [chars, probs]


def GenerateGibberish(bigramStruct, length):
    k = list(bigramStruct.keys())
    
    charDist = GetCharacterDistribution(corpus)
    priorChar = rand.choice(charDist[0],1,True,charDist[1])[0]
    gibberishString = str(priorChar)
    for i in range(length-1):
        transitionDict = bigramStruct[priorChar]
        transitionProbs = list(transitionDict.values())
        priorChar = rand.choice(k,1,True, transitionProbs)[0]
        gibberishString = gibberishString + str(priorChar)
    return gibberishString

    
def Main(corpus):
    bigramStruct = GenerateBigramDictionary(corpus)
    gibberishSample = GenerateGibberish(bigramStruct, 200)
    return gibberishSample







