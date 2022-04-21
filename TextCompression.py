import Frequence as fr
import Codage as cod
import BinaryTree as bt

doc = str(input("Quel texte voulez-vous compresser ? "))
doc2 = doc+".txt"
taille_alphabet = str(len(fr.alphabet(doc2)))

with open(doc+"_freq.txt", "w") as file:
    file.write(taille_alphabet+"\n")
    d = fr.dict_frequences(doc2)
    for char in d.items():
        if char[0] == "\n":
            file.write("LINE FEED "+str(char[1])+"\n")
        elif char[0] == " ":
            file.write("SPACE "+str(char[1])+"\n")
        else:
            file.write(str(char[0])+" "+str(char[1])+"\n")

with open(doc+"_comp.bin", "w") as file:
    c = cod.Codage(bt.BTree(doc2))
    c.dic_codage_caractere(c.arbre.get_root())
    compressed_text = c.codage_texte()
    file.write(compressed_text)
