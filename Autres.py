import BinaryTree as bt
import Frequence as f

def liste_frequences(document):
    l=[]
    for cara in f.alphabet(document):
        freq=[]
        freq.append(cara)
        nb=0
        file = open(document, "r")
        for line in file:
            for letter in line:
                if cara == letter.lower():
                    nb+=1
        freq.append(nb)
        l.append(freq)
    file.close()
    return dict(sorted(l, key=lambda element: element[1]))

def ParcoursProfondeur(arbre):
    l = []
    m = []
    l.append(arbre.get_root())
    while (l != []):
        n = l[len(l)-1]
        l.pop(len(l)-1)
        m.append(n.label)
        if (n.getRight() != None):
            l.append(n.getRight())
        if (n.getLeft() != None):
            l.append(n.getLeft())
    return m

def ParcoursProfondeurBit(arbre, caractere):
    ch = ''
    l = []
    l.append(arbre.get_root())
    while (l != []):
        n = l[len(l)-1]
        l.pop(len(l)-1)
        while (n.getRight() != None):
            l.append(n.getRight())
            ch += '1'
            if n.getRight().getCaractere() == caractere:
                return ch
            n = n.getRight()
        while (n.getLeft() != None):
            l.append(n.getLeft())
            ch += '0'
            if n.getLeft().getCaractere() == caractere:
                return ch
            n = n.getLeft()
    

'''           
def ParcoursLargeur(arbre, caractere):
    l = []
    m = []
    l.append(arbre.get_root())
    while (l != []):
        n = l[0]
        l.pop(0)
        m.append(n.label)
        if (n.getLeft() != None):
            l.append(n.getLeft())
        if (n.getRight() != None):
            l.append(n.getRight()) 
    return m
'''

# print(ParcoursProfondeur(bt.BTree("exemple.txt")))
# print(ParcoursLargeur(bt.BTree("exemple.txt"), "c"))
# print(ParcoursProfondeurBit(bt.BTree("exemple.txt"), "b"))