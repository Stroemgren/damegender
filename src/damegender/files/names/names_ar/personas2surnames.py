#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2022 David Arroyo Menendez

#  Author: David Arroyo Menendez <darroyome@MacBook-Pro-de-David.local> 
#  Maintainer: David Arroyo Menendez <darroyome@MacBook-Pro-de-David.local> 
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
# 
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with Damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,


import csv

with open('personas.csv') as csvfile:
    sreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    next(sreader, None)
    filesurnames = open('arsurnames.csv','w')
    diccsurnames = {}
    for row in sreader:
        if row[2] in diccsurnames.keys():
                diccsurnames[row[2]] = diccsurnames[row[2]] + 1
        else:
                diccsurnames[row[2]] = 1
        
    for i in diccsurnames.keys():
        filesurnames.write(str(i)+","+str(diccsurnames[i])+"\n")
    
filesurnames.close()

