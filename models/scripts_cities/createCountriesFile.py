#!/usr/bin/env python3

with open("countries", "r") as filin:
    ligne = filin.readline()
    while ligne != "":
        print(ligne)
        file = open("cities/{}".format(ligne), "w")
        file.close()
        ligne = filin.readline()
