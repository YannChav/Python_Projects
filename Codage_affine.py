# -*- coding: utf-8 -*-

def coder_lettre(lettre, a, b):
    tab_lettres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
                   "P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(len(tab_lettres)):
        if lettre == tab_lettres[i]:
            x = i
            break
    ind_lettre = (a * x + b) % 26
    lettre = tab_lettres[ind_lettre]
    return lettre

def coder_mot(mot, a, b):
    mot_code = ""
    for lettre in mot:
        lettre_codee = coder_lettre(lettre, a, b)
        mot_code += lettre_codee
    return mot_code
        
test = coder_mot("BRAVO", 3, 4)
print(test)



def decoder_lettre(lettre, a, b, u):
    tab_lettres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
                   "P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(len(tab_lettres)):
        if lettre == tab_lettres[i]:
            y = i
            break
    ind_lettre = (u * y - b * u) % 26
    lettre = tab_lettres[ind_lettre]
    return lettre

def decoder_mot(mot, a, b):
    mot_decode = ""
    phrase_u = a, '*u est congru à 1 modulo 26, combien vaut u ?'
    u = int(input(phrase_u))
    for lettre in mot:
        lettre_decodee = decoder_lettre(lettre, a, b, u)
        mot_decode += lettre_decodee
    return mot_decode

test = decoder_mot("HDEPU", 3, 4)
print(test)