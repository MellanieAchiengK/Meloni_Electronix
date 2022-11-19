#!/usr/bin/env python3
import os

os.getcwd()
PATH_COUNTIRES_FILE = os.getcwd() + '/models/scripts_cities/countries'

listeFile = []

def liste_Files():
    with open(PATH_COUNTIRES_FILE, "r") as filin:
        ligne = filin.readline()
        while ligne != "":
            listeFile.append(ligne)
            ligne = filin.readline()

    return listeFile
