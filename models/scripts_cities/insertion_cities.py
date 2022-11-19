#!/usr/bin/python3

from listeFile import liste_Files
from models import storage
from models.city import City
import os
from os import listdir
from os.path import isfile, join

os.getcwd()
PATH_COUNTIRES_FILE = os.getcwd() + '/models/scripts_cities/countries'
PATH_FILE_BY_CONTRIES = os.getcwd() + '/models/scripts_cities/cities'
files_countries = [f for f in listdir(PATH_FILE_BY_CONTRIES) if isfile(join(PATH_FILE_BY_CONTRIES, f))]


id = 1
cityDb_all = []
for loop in storage.all(City).values():
    cityDb_all.append(loop.to_dict().get("name"))

for country in sorted(files_countries):
    cities_all = liste_Files(PATH_FILE_BY_CONTRIES + "/" + country)
    if cities_all is not None:
        for cit in cities_all:
            if cit not in cityDb_all:
                city = City(name=cit, country_id=id)
                city.save()
                print(city.to_dict())
            else:
                print("<{}> already exists".format(cit))
    id += 1

