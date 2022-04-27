import Frequence as fr

#Etape 2: Construction de l’arbre

'''
Il faut d'abord créer une classe pour les noeuds nécessaire pour créer la classe BTree permettant de construire l'arbre de Huffman
'''

class BNode():
    def __init__(self, freq, label=None, leftChild=None, rightChild=None):
        self.freq = freq
        self.label = label
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def getOccurence(self):
        return self.freq
    def getCaractere(self):
        return self.label
    def getLeft(self):
        return self.leftChild
    def getRight(self):
        return self.rightChild


class BTree():
    def __init__(self, document):

        self.document = document

        #on créé une liste de noeuds tel que chaque noeud contient le caractère et sa fréquence pour le document choisi
        node_list = [BNode(freq, label) for label, freq in fr.dict_frequences(document).items()]

        while len(node_list) > 1:
            #on trie la liste à chaque itération selon les fréquences croissantes pour pouvoir récuperer plus facilement les 2 noeuds de fréquence minimale(indice 0 de la liste)
            node_list = sorted(node_list, key=lambda node: node.freq)
            left_node = node_list.pop(0)
            right_node = node_list.pop(0)
            parent_node = BNode(left_node.getOccurence() + right_node.getOccurence())
            parent_node.leftChild = left_node
            parent_node.rightChild = right_node
            node_list.append(parent_node)
            
        #le noeud racine de l'arbre sera alors le premier élément de la liste node_list
        self.root = node_list[0]

    def get_root(self):
        return self
