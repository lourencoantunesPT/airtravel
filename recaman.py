import sys
from itertools import count, islice

def generate_sequence():
    """ gera serie recaman"""
    visto = set()
    a = 0
    for n in count(1):
        yield a
        visto.add(a)
        c = a-n
        if c < 0 or c in visto:
            c = a + n
        a = c


def write_sequence(filename, num):
    """ escreve a serie para um ficheiro"""
    f = open(filename, mode = 'wt')
    f.writelines(f"{r}\n" for r in islice(generate_sequence(), num + 1 ))
    f.close()

print( __name__ )
if __name__ == '__main__':
    pass
print(sys.argv[1])
print(sys.argv[2])
write_sequence(filename=sys.argv[1], num=int(sys.argv[2]))
