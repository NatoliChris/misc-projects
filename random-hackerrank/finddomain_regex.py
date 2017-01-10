#!/usr/bin/env python3
import re

def get_web_from_line(line, fin):
    reg = r'https{0,1}:\/\/([a-z0-9]+\.)+[a-z]+'
    ag = re.finditer(reg, line)
    for i in ag:
        fin.add(i.group(0).replace('http://','').replace('https://','').replace('www.',''))

    return fin
def main():
    fin = set()
    linenum = int(input())
    for i in range(linenum):
        lin = input()
        fin = get_web_from_line(lin, fin)
    a = list(fin)
    a.sort()
    print(";".join(str(j) for j in a))

if __name__ == '__main__':
    main()
