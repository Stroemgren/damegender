#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is Free Software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# DESCRIPTION: Given a surname returns people using it in Spain or
# United States of America

from app.dame_gender import Gender
from app.dame_wikidata import DameWikidata
from app.dame_ethnicity import DameEthnicity
import sys
import os
import re
import argparse

dw = DameWikidata()
isocodes = dw.dicc_countries().keys()
codes = list(isocodes) + ["inter", "ine"]
parser = argparse.ArgumentParser()
parser.add_argument("surname", help="display the gender")
parser.add_argument('--total', required=True,
                    default="es", choices=codes)
parser.add_argument('--spanish_provinces', default=False,
                    action="store_true")
parser.add_argument('--version', action='version', version='0.3')
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()


de = DameEthnicity()
if (args.total == "inter"):
    country = "the International Dataset"
else:
    country = de.iso3166_to_eng(args.total)

results = []

g = Gender()
v = g.guess_surname(args.surname, args.total)

if v[0]:
    bool1 = args.total in isocodes
    bool2 = ((args.total == 'es') or (args.total == 'ine'))
    if (args.total == "inter"):
        print("There are %s people using %s in %s"
              % (v[1], args.surname, country))
    elif bool2:
        print("There are %s people using %s in Spain"
              % (v[1], args.surname))
        if (args.spanish_provinces):
            string1 = """
The next data is only for the 50 most frequently first
surnames located by place where the person is living
"""
            print(string1)

            frec1 = g.inesurname_province_and_frec(args.surname,
                                                   province='acorugna')
            print("A Coruña: %s" % frec1)
            frec2 = g.inesurname_province_and_frec(args.surname,
                                                   province='alava')
            print("Alava: %s" % frec2)
            frec3 = g.inesurname_province_and_frec(args.surname,
                                                   province='albacete')
            print("Albacete: %s" % frec3)
            frec4 = g.inesurname_province_and_frec(args.surname,
                                                   province='alicante')
            print("Alicante: %s" % frec4)
            frec5 = g.inesurname_province_and_frec(args.surname,
                                                   province='almeria')
            print("Almeria: %s" % frec5)
            frec6 = g.inesurname_province_and_frec(args.surname,
                                                   province='asturias')
            print("Asturias: %s" % frec6)
            frec7 = g.inesurname_province_and_frec(args.surname,
                                                   province='avila')
            print("Ávila: %s" % frec7)
            frec8 = g.inesurname_province_and_frec(args.surname,
                                                   province='badajoz')
            print("Badajoz: %s" % frec8)
            frec9 = g.inesurname_province_and_frec(args.surname,
                                                   province='baleares')
            print("Baleares: %s" % frec9)
            frec10 = g.inesurname_province_and_frec(args.surname,
                                                    province='barcelona')
            print("Barcelona: %s" % frec10)
            frec11 = g.inesurname_province_and_frec(args.surname,
                                                    province='bizkaia')
            print("Bizkaia: %s" % frec11)
            frec12 = g.inesurname_province_and_frec(args.surname,
                                                    province='burgos')
            print("Burgos: %s" % frec12)
            frec13 = g.inesurname_province_and_frec(args.surname,
                                                    province='caceres')
            print("Cáceres: %s" % frec13)
            frec14 = g.inesurname_province_and_frec(args.surname,
                                                    province='cadiz')
            print("Cádiz: %s" % frec14)
            frec15 = g.inesurname_province_and_frec(args.surname,
                                                    province='cantabria')
            print("Cantabria: %s" % frec15)
            frec16 = g.inesurname_province_and_frec(args.surname,
                                                    province='castellon')
            print("Castellon: %s" % frec16)
            frec17 = g.inesurname_province_and_frec(args.surname,
                                                    province='ceuta')
            print("Ceuta: %s" % frec17)
            frec18 = g.inesurname_province_and_frec(args.surname,
                                                    province='ciudadreal')
            print("Ciudad Real: %s" % frec18)
            frec19 = g.inesurname_province_and_frec(args.surname,
                                                    province='cordoba')
            print("Córdoba: %s" % frec19)
            frec20 = g.inesurname_province_and_frec(args.surname,
                                                    province='cuenca')
            print("Cuenca: %s" % frec20)
            frec21 = g.inesurname_province_and_frec(args.surname,
                                                    province='girona')
            print("Girona: %s" % frec21)
            frec22 = g.inesurname_province_and_frec(args.surname,
                                                    province='granada')
            print("Granada: %s" % frec22)
            frec23 = g.inesurname_province_and_frec(args.surname,
                                                    province='guadalajara')
            print("Guadalajara: %s" % frec23)
            frec24 = g.inesurname_province_and_frec(args.surname,
                                                    province='guipuzkoa')
            print("Guipuzkoa: %s" % frec24)
            frec25 = g.inesurname_province_and_frec(args.surname,
                                                    province='huelva')
            print("Huelva: %s" % frec25)
            frec26 = g.inesurname_province_and_frec(args.surname,
                                                    province='huesca')
            print("Huesca: %s" % frec26)
            frec27 = g.inesurname_province_and_frec(args.surname,
                                                    province='jaen')
            print("Jaen: %s" % frec27)
            frec28 = g.inesurname_province_and_frec(args.surname,
                                                    province='larioja')
            print("La Rioja: %s" % frec28)
            frec29 = g.inesurname_province_and_frec(args.surname,
                                                    province='leon')
            print("Leon: %s" % frec29)
            frec30 = g.inesurname_province_and_frec(args.surname,
                                                    province='leon')
            print("Leon: %s" % frec30)
            frec31 = g.inesurname_province_and_frec(args.surname,
                                                    province='lleida')
            print("Lleida: %s" % frec31)
            frec33 = g.inesurname_province_and_frec(args.surname,
                                                    province='lugo')
            print("Lugo: %s" % frec33)
            frec34 = g.inesurname_province_and_frec(args.surname,
                                                    province='madrid')
            print("Madrid: %s" % frec34)
            frec35 = g.inesurname_province_and_frec(args.surname,
                                                    province='malaga')
            print("Málaga: %s" % frec35)
            frec36 = g.inesurname_province_and_frec(args.surname,
                                                    province='melilla')
            print("Melilla: %s" % frec36)
            frec37 = g.inesurname_province_and_frec(args.surname,
                                                    province='murcia')
            print("Murcia: %s" % frec37)
            frec38 = g.inesurname_province_and_frec(args.surname,
                                                    province='navarra')
            print("Navarra: %s" % frec38)
            frec39 = g.inesurname_province_and_frec(args.surname,
                                                    province='ourense')
            print("Ourense: %s" % frec39)
            frec40 = g.inesurname_province_and_frec(args.surname,
                                                    province='palencia')
            print("Palencia: %s" % frec40)
            frec41 = g.inesurname_province_and_frec(args.surname,
                                                    province='pontevedra')
            print("Pontevedra: %s" % frec41)
            frec42 = g.inesurname_province_and_frec(args.surname,
                                                    province='salamanca')
            print("Salamanca: %s" % frec42)
            frec43 = g.inesurname_province_and_frec(args.surname,
                                                    province='segovia')
            print("Segovia: %s" % frec43)
            frec44 = g.inesurname_province_and_frec(args.surname,
                                                    province='sevilla')
            print("Sevilla: %s" % frec44)
            frec45 = g.inesurname_province_and_frec(args.surname,
                                                    province='soria')
            print("Soria: %s" % frec45)
            frec46 = g.inesurname_province_and_frec(args.surname,
                                                    province='tarragona')
            print("Tarragona: %s" % frec46)
            frec47 = g.inesurname_province_and_frec(args.surname,
                                                    province='tenerife')
            print("Tenerife: %s" % frec47)
            frec48 = g.inesurname_province_and_frec(args.surname,
                                                    province='teruel')
            print("Teruel: %s" % frec48)
            frec49 = g.inesurname_province_and_frec(args.surname,
                                                    province='toledo')
            print("Toledo: %s" % frec49)
            frec50 = g.inesurname_province_and_frec(args.surname,
                                                    province='valencia')
            print("Valencia: %s" % frec50)
            frec51 = g.inesurname_province_and_frec(args.surname,
                                                    province='valladolid')
            print("Valladolid: %s" % frec51)
            frec52 = g.inesurname_province_and_frec(args.surname,
                                                    province='zamora')
            print("Zamora: %s" % frec52)
            frec53 = g.inesurname_province_and_frec(args.surname,
                                                    province='zaragoza')
            print("Zaragoza: %s" % frec53)

            string2 = """
The previous data is only for the 50 most frequently first
surnames located by place where the person is living
"""
            print(string2)
    elif bool1:
        print("There are %s people using %s in %s"
              % (v[1], args.surname, country))
else:
    print("It has not been found %s in %s"
          % (args.surname, country))

if (args.total in g.config['DATASET']['official_surnames']):
    print("Source: Official Statistics in %s" % (country))
elif (args.total == "inter"):
    print("Source: Official Statistics and Wikidata")
    print("(retrieved betwen March and April (2022)")
else:
    print("Source: Wikidata (retrieved betwen March and April (2022)")
