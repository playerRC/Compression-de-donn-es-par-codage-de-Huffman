import Frequence as fr
import Codage as cd
import BinaryTree as bt

def volume_initial(doc):
    nb=0
    file = open(doc, "r")
    for line in file:
        for caracter in line:
            nb += 1
    return nb

def volume_finale(doc):
    bit1 = 0
    bit2 = 8 * len(fr.alphabet(doc))
    cod = cd.Codage(bt.BTree(doc))
    d1 = fr.dict_frequences(doc)
    d2 = cod.dic_codage_caractere(cod.arbre.get_root())
    for cle in d2:
        bit1 += len(d2[cle]) * d1[cle]
    for cle in d2:
        bit2 += len(d2[cle])
    return (bit1 + bit2)/8

def ratio(doc):
    return 1 - (volume_finale(doc)/volume_initial(doc))

print(ratio("exemple.txt"))
gain_volume = ratio("exemple.txt") * volume_initial("exemple.txt")
print(gain_volume)


# pour vol_ini et final : https://www.youtube.com/watch?v=co4_ahEDCho