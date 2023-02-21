# files.py

import sys
from sys import *


f=open(sys.argv[1], mode = 'rt', encoding='utf-8')
#usando o print(), escreve o \n\r o que leva a duplicar salto em cada linha (linha em branco entre cada linha)
for line in f:
    print(line)

print ("--------------------------------")

f.seek(0)
for line in f:
    sys.stdout.write(line)

f.close()


