#!/usr/bin/env python

import sys

zaglavlje = "Hyp"
for i in range(10,100,10):
    zaglavlje += "#Q"+str(i)

print(zaglavlje)

brojac = 0

dat = open("ulaz2.txt")

for redak in dat:
    ispis = ''
    lista = []
    
    brojac += 1
    ispis += str(brojac).zfill(3) # formatirati brojac na ###

    lista = redak.rstrip().split( )
    lista = [float(y) for y in lista]
    lista.sort()

    for i in range(10,100,10):
        x = (i/float(100))*len(lista)
        ispis += "#"+str(lista[int(x)])

    print(ispis)

dat.close()
