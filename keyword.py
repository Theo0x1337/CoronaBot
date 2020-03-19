#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 22:09:39 2020

@author: bernardintheo
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist


class KeyWordCity :
    
    def __init__(self,chaine):
        self.content = chaine
        
        
        
    def getKeywordsCity(self):
        stop_words = set(stopwords.words('french'))
        
        tokenizer = RegexpTokenizer(r"\w+")
        new_words = tokenizer.tokenize(self.content)
        
        chInter = ""
        
        for elem in new_words: 
            chInter = chInter +" "+ elem
        
        words = word_tokenize(chInter)
         
        new_sentence = ""
                 
        for word in words:
            if word not in ['RT','https','t','co','le','que','on','ça','a','T ','T','J','J ','Je','je','va','Le','L','coronavirus','covid19',
                            'rt','là','quand','songroku1','corona','virus']:
                if word not in stop_words:
                    new_sentence = new_sentence +" "+ word
         
            
        stFinal = tokenizer.tokenize(new_sentence)
        
        return stFinal
    
    
    def get10TopKeyWords(self,tabWord):
        allWordDist = FreqDist(tabWord)
        allWordDist.plot(20)


chaine = ""
with open("data_corona1.txt","r") as f:
    chaine = f.read()
    
chaineFinal = ""
for char in chaine:
    chaineFinal = chaineFinal + char.lower()
    
kw = KeyWordCity(chaineFinal)

tabMots = kw.getKeywordsCity()

print(len(tabMots))

kw.get10TopKeyWords(tabMots)