# -*- coding: utf-8 -*-

#II Implementation codage Huffman

#1) table occurence

def table_frequences(txt):
    """Cette fonction prend en entrée une chaine de caractères et retourne un 
    dictionnaire contenant le nombre d'occurences de chaque lettre."""
    assert(isinstance(txt, str)), "Une chaine de caractère est prise en argument"
    dico = {}
    for i in range(len(txt)):
        cles = dico.keys() 
        if txt[i] in cles:
            dico[txt[i]] = dico[txt[i]] + 1
        else:
            dico[txt[i]] = 1
    return dico

#test = table_frequences('PROGRAMMATION EN LANGAGE PYTHON')
#print(test)
    

#2) Classe arbre d'Huffman

class Arbre_huffman:
    """Créé un arbre d'Huffman."""
    
    def __init__(self, let=None, occ=None, g=None, d=None):
        self.lettre = let
        self.occurence = occ
        self.gauche = g
        self.droite = d
        
    def feuille(self):
        """Cette méthode retourne True si l'arbre est une feuille."""
        return self.gauche is None and self.droite is None
    
    def __It__(self, autre_arbre):
        """Cette méthode retourne True si l'arbre est strictement inférieur à 
        un autre arbre."""
        return self.occurence > autre_arbre.occurence
    
    
#3) Construction feuilles de l'arbre
        
def listes_feuilles_arbre(texte):
    """Cette fonction prend en paramètre une chaine de caractère texte et 
    retourne une liste triée liste_arbres constituée d'objets Arbre_Huffman 
    correspondant aux feuilles de notre arbre final."""
    dico = table_frequences(texte)
    liste_arbres = [Arbre_huffman(cles, dico[cles]) for cles in dico.keys()]
    liste_arbres.sort(reverse = True, key = lambda element : element.occurence)
    return liste_arbres


#4) Arbre complet

def arbre_huffman(texte):
    """Cette fonction retourne une liste composée d'un arbre unique, l'arbre 
    d'Huffman."""
    liste_feuille = listes_feuilles_arbre(texte)
    while len(liste_feuille) != 1:
        arbre_somme = Arbre_huffman(None, liste_feuille[-1].occurence + liste_feuille[-2].occurence, liste_feuille[-2], liste_feuille[-1])
        del liste_feuille[-2]
        del liste_feuille[-1]
        liste_feuille.append(arbre_somme)
        liste_feuille.sort(reverse = True, key = lambda element : element.occurence)
    arbre_huffman = liste_feuille[0]
    return arbre_huffman

#texte = 'PROGRAMMATION EN LANGAGE PYTHON'
#arbre_huff = arbre_huffman(texte)
#print(arbre_huff)


#5) Code binaire

def parcours_postfixe(arbre, chemin_en_cours, dico):
    if arbre == None:
        return {}
    else:
        if arbre.feuille():
            dico[arbre.lettre] = chemin_en_cours
        else:
            parcours_postfixe(arbre.gauche, chemin_en_cours + '0', dico)
            parcours_postfixe(arbre.droite, chemin_en_cours + '1', dico)
    return dico
    
#texte = 'PROGRAMMATION EN LANGAGE PYTHON'
#arbre_huff = arbre_huffman(texte)
#dico = {}
#parcours_postfixe(arbre_huff,'', dico)
#print(dico)


#6) Codage et décodage

def coder(txt, dico):
    code = ''
    for i in range(len(txt)):
        code += dico[txt[i]] + " "
    return code

def decoder(code, dico):
    texte = ''
    code_huff = ''
    for i in range(len(code)):
        if code[i] != ' ':
            code_huff += code[i]
        else:
            lettres = dico.keys()
            for i in lettres:
                if dico[i] == code_huff:
                    texte += i
            code_huff = ''
    return texte

# faire attention à avoir le fichier poeme.txt
with open("poeme.txt", "r", encoding = "utf-8") as fichier:
    texte = fichier.read()
# texte = "PROGRAMMATION EN LANGAGE PYTHON"
    
table = table_frequences(texte)
print(table)

arbre_huff = arbre_huffman(texte)
dico = {}
dico_caractere = parcours_postfixe(arbre_huff,'', dico)
print(dico_caractere)

code = coder(texte, dico_caractere)
print(code)  

texte = decoder(code, dico_caractere)
print(texte)  


#7) Code entier
    
#Calcul taille en ASCII
nbr_lettres = 0
for lettre in texte:
    nbr_lettres += 1
    
poids_txt = nbr_lettres * 8
print("la taille de ce texte en code ASCII est de ", poids_txt, "bits.")

#Calcul taille compressée
arbre_huff = arbre_huffman(texte)
dico = {}
parcours_postfixe(arbre_huff,'', dico)
code = coder(texte, dico)


nbr_bits = 0
for bits in code:
    if bits == '0' or bits == '1':
        nbr_bits += 1
print("La taille de ce texte en codage Huffman est de ", nbr_bits, "bits.")

#Calcul du taux de compression
taux = (poids_txt - nbr_bits) / poids_txt * 100
print("Le taux de compression du texte est de ", taux, "%")