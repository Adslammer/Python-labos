#!/usr/bin/env python

import os

dat = open("studenti.txt")

podaci = {}
for redak in dat:
    red = redak.rstrip().split( )
    podaci[red[0]] = red[1]
	
dat.close()

bodovi = {}
rbr_max = 0

datoteke = os.listdir("./zadatak3")
for datoteka in datoteke:
    pom = datoteka.split(".")
    pom = pom[0].split("_")
    rbr = int(pom[1])

    if (rbr > rbr_max):
        rbr_max = rbr

    dat = open("zadatak3/"+datoteka)

    for line in dat:

        zapis = line.rstrip().split( )
        jmbag = zapis[0]
        if (rbr,zapis[0]) in bodovi:
            print("Prepisivanje preko podataka!")
        else:
            bodovi[(rbr,zapis[0])] = zapis[1] # (broj labosa, jbmag) = bodovi

    dat.close()

# formatiranje
jmbag = '%-12s' % 'JMBAG'
prez_ime = '%-20s' % 'Prezime,Ime'

labosi = ''
for i in range(1,rbr_max+1):
    pom = "L"+str(i)
    labosi += '%9s' % pom

print(jmbag,prez_ime,labosi)

for key in podaci:
    jmbag = '%-12s' % key
    prez_ime = '%-20s' % podaci[key]

    labosi = ''   
    for i in range(1,rbr_max+1):
        if (i,key) in bodovi:
            labosi += '%9s' % str(bodovi[(i,key)])
        else:
            labosi += '%9s' % '0'

    print(jmbag,prez_ime,labosi)