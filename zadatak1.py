#!/usr/bin/env python

import sys

def citajMat(dat):

    matrica = {}

    redak1 = dat.readline().strip().split( )

    if (len(redak1) != 2):
        print("krivi broj u prvom retku zapisa tablice")
        sys.exit(1)
    
    x = int(redak1[0])
    y = int(redak1[1])

    while 1:
        redak = dat.readline().strip()
        if ((not redak) or (redak == "")):
            return x, y, matrica
        else:
            pom = redak.split( )
            
            if (len(pom) != 3):
                print("redak matrice nije dobro zadan")
                sys.exit(2)

            elif (int(pom[0])>x or int(pom[1])>y):
                print("element je izvan matrice")
                sys.exit(3)
                
            matrica[(int(pom[0]),int(pom[1]))] = float(pom[2])
    
    return x, y, matrica

dat = open("ulaz.txt")
#dat = open(sys.argv[1])

x1, y1, matrica1 = citajMat(dat)
x2, y2, matrica2 = citajMat(dat)

dat.close()

if (y1 != x2):
    print("matrice nisu pogodne za medusobno mnozenje")
    sys.exit(3)

matrica3 = {}

for i in range(1,x1+1):
    for j in range(1,y2+1):
        for k in range(1,x2):
            if ((i,k) in matrica1 and (k,j) in matrica2):
                if ((i,j) in matrica3):
                    matrica3[(i,j)] += matrica1[(i,k)]*matrica2[(k,j)]
                else:
                    matrica3[(i,j)] = matrica1[(i,k)]*matrica2[(k,j)]

dat = open("izlaz.txt","w+")
#dat = open(sys.argv[2],"w+")

dat.write(str(x1)+" "+str(y2)+"\n")

for key in matrica3:
    dat.write(str(key[0])+" "+str(key[1])+" "+str(matrica3[key]).rstrip('.0')+"\n")
    print(key[0],key[1], matrica3[key])

dat.close()