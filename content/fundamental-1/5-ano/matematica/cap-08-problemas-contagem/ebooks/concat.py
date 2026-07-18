import os

parts = ['part1.md', 'part2.md', 'part3.md']
with open('ef05ma09-exercicios.md', 'w', encoding='utf-8') as outfile:
    for p in parts:
        with open(p, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
            outfile.write("\n")
        os.remove(p)
os.remove('concat.py')
