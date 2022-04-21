# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:00:53 2022

@author: faskar
"""

#Etape 1

def alphabet(document):
    l=[]
    file = open(document, "r")
    for line in file:
        for caracter in line:
           if caracter not in l:
                l.append(caracter)
    file.close()
    return l

def dict_frequences(document):
    dic = {}
    for caractere in alphabet(document):
        nb=0
        file = open(document, "r")
        for line in file:
            for letter in line:
                if letter == caractere:
                    nb+=1
        dic[caractere] = nb
    file.close()
    return dict(sorted(dic.items(), key=lambda frequence: frequence[1]))
    

    
#print(dict_frequences('textesimple.txt'))





# http://cermics.enpc.fr/polys/info1/main/node76.html
# https://python-prepa.github.io/information_theory.html



