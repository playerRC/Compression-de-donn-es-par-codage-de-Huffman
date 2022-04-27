import os
import Frequence as fr
import Codage as cod
import BinaryTree as bt
import CompressionRatio as cr

print("\n----BIENVENUE DANS LE COMPRESSEUR DE FICHIER TXT----\n")

doc = str(input("Quel texte voulez-vous compresser ? "))
doc2 = doc+".txt"
while os.path.exists(doc2) == False:
    print("\nLe fichier à compresser n'est pas dans le bon dossier\n")
    doc = str(input("Quel texte voulez-vous compresser ? "))
    doc2 = doc+".txt"

taille_alphabet = str(len(fr.alphabet(doc2)))

'''
La fonction suivante permet de connaître l'ordre d'apparition des caractères et est utile si l'on veut décoder le fichier .bin
'''
def ordreApparitionCaractere(document):
    l =[]
    file = open(document, "r")
    for line in file:
        for letter in line:
            l.append(letter)
    file.close()
    return l

with open(doc+"_freq.txt", "w") as file:
    file.write(taille_alphabet+"\n")
    l = fr.liste_frequences(doc2)
    for char in l:
        if char[0] == "\n":
            file.write("LINE FEED "+str(char[1])+"\n")
        elif char[0] == " ":
            file.write("SPACE "+str(char[1])+"\n")
        else:
            file.write(str(char[0])+" "+str(char[1])+"\n")

with open(doc+"_comp.bin", "w") as file:
    c = cod.Codage(bt.BTree(doc2))
    dict_codage_caractere = c.dic_codage_caractere(c.arbre.get_root())
    compressed_text = c.codage_texte()
    file.write(compressed_text)

print(f'''\nL'ordre d'apparition des caractères dans le texte est le suivant: {ordreApparitionCaractere(doc2)}
Dictionnaire du nombre d'apparitions de chaque caractère: {fr.dict_frequences(doc2)}
Dictionnaire du codage de chaque caractère: {dict_codage_caractere}
Taux de compression atteint: {cr.ratio(doc2)}
Nombre moyen de bits de stockage d’un caractère: {cr.nb_bits_moyen(doc2)}\n'''
)
