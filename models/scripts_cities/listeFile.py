#!/usr/bin/env python3
import os



def liste_Files(file):
    listeFile = []
    with open(file, "r") as filin:
        ligne = filin.readline()
        while ligne != "":
            ligne = ligne[:len(ligne) - 1]
            listeFile.append(ligne.upper())
            ligne = filin.readline()
    filin.close()
    return sorted(listeFile)
