
### IO operations in Python

import sys

###
sys.getdefaultencoding()


f = open("exemplo.txt", mode='wt', encoding='utf-8')
# f é do tipo _io.TextIOWrapper

f.write("--- ola tas bom\n")
f.write("--- eu estou bem e tu? \n")
f.write("--- tudo fixe\n")
f.close()
# escreve por cima do ficheiro


g = open("exemplo.txt", 'rt')
print ("ler 10 carateres")
print(g.read(10))
print("ler tudo")
print(g.read())
print("ler tudo com posicionamento no inicio")
g.seek(0)
print(g.read())
g.close()

m = open("exemplo.txt", 'rt')
print ("ler linha")
print(m.readline())
print ("ler outra linha")
print(m.readline())
print ("ler as linhas todas de uma vez com readlines()")
m.seek(0)
print(m.readlines())

m.close()








