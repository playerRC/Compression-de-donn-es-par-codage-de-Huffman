import BinaryTree as bt

# Etape 3

class Codage():
    def __init__(self, arbre):
        self.arbre = arbre
        self.codage = {}

    def dic_codage_caractere(self, node, code_actuel = ""):
        if node == None:
            return
        if node.getCaractere() != None:
            self.codage[node.getCaractere()] = code_actuel
        self.dic_codage_caractere(node.leftChild, code_actuel + "0")
        self.dic_codage_caractere(node.rightChild, code_actuel + "1")
        return self.codage
    
    def codage_texte(self):
        doc = self.arbre.document
        ch = ''
        file = open(doc, "r")
        for line in file:
            for caractere in line:
                ch += self.codage[caractere]
        file.close()
        return ch

'''
c = Codage(bt.BTree("exemple.txt"))
print(c.dic_codage_caractere(c.arbre.get_root()))
print(c.codage_texte())
'''