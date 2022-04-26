# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:00:53 2022
@author: faskar
"""

#Etape 1: Détermination de l’alphabet et des fréquences de caractères

'''
La fonction alphabet permet de déterminer tous les caractères présents dans le texte
Cette fonction est nécessaire pour établir un dictionnaire avec le nombre d'occurences pour chaque caractère
Elle nous sera également utile pour afficher la taille de l’alphabet dans le fichier <nom>_freq.txt
'''

def alphabet(document):
    l=[]
    file = open(document, "r")
    for line in file:
        for caracter in line:
           if caracter not in l:
                l.append(caracter)
    file.close()
    return l

'''
On créé une fonction permettant de renvoyer un dictionnaire avec le nombre d'occurences de chaque caractère trié dans l'ordre croissant des fréquences.
Ce tri est nécessaire pour pouvoir ensuite construire l'arbre de Huffman.
'''

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
    
'''
La fonction suivante nous sera utile pour générer le fichier se terminant par _freq.txt car contrairement à la précédente elle trie les caracères
selon leur fréquence puis selon l'ordre ASCII donc cela nous permettra de créer ce fichier plus simplement.
'''
    
def liste_frequences(document):
    l=[]
    for cara in alphabet(document):
        freq=[]
        freq.append(cara)
        nb=0
        file = open(document, "r")
        for line in file:
            for letter in line:
                if letter == cara:
                    nb+=1
        freq.append(nb)
        l.append(freq)
    file.close()
    l.sort(key=lambda row: (row[1], row[0]))
    return l
