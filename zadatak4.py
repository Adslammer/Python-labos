#!/usr/bin/env python

import sys
import urllib.request
import re

#if (len(sys.argv) != 2):
#    print("Krivi broj argumenata!")
#    sys.exit(1)
    
#url = sys.argv[1]
url = "http://www.fer.unizg.hr"

site = urllib.request.urlopen(url)

##site = urllib2.urlopen("http://www.net.hr")

page = site.read().decode("utf8")
print(page)

# trazenje linkova
lista_linkova = re.findall("href=\"(.+?)\"",page)

print("\n\n\n\n\nLinkovi")

lista_hostova = []
ponavljanje_hosta = {}

for link in lista_linkova:
    print(link)
    host = re.match(r"^(http|ftp|https|ftps)://(?P<naziv>[\w\.-]+)/",link)
    
    if (host):
        if (host.group('naziv') not in lista_hostova):
            lista_hostova.append(host.group('naziv'))
            ponavljanje_hosta[host.group('naziv')] = 1
        else:
            ponavljanje_hosta[host.group('naziv')] += 1
            
    
# trazenje mailova
lista_mailova = re.findall("[\w\.-]+@[\w\.-]+",page)

print("\n\n\n\n\nMailovi")

for mail in lista_mailova:
    print(mail)

# linkovi na slike
lista_slika = re.findall("<img src=\"(.+?)\"",page)
broj_slika = len(lista_slika)
print("\n\n\n\n\nBroj linkova na slike")
print(broj_slika)
