#!/usr/bin/python3

from listeFile import liste_Files
from models import storage
from models.city import City
import os

os.getcwd()
PATH_FILE_BY_CONTRIES = os.getcwd() + '/models/scripts_cities/cities'


id = 1
for country in liste_Files():
    #print(id," ",country)
    with open(PATH_FILE_BY_CONTRIES + "/" + country, "r") as filin:
        ligne = filin.readline()
        while ligne != "":
            print(ligne)
            if ligne is not None:
                city = City(name=ligne, country_id=id)
                print(city.to_dict())

            ligne = filin.readline()
    id += 1

