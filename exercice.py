#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot2=""
    for lettre in mot:
        num=ord(lettre)
        num-=32
        mot2=mot2+chr(num)
    return mot2

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
