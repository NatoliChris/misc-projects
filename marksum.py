#!/usr/bin/env python3

import math

def main():
    count = 0
    while(1):
        try:
            num = input()
            x = int(num)
        except:
            break
        if(x == -1):
            break
        count = count + x
    print(count)

#if __name__ == "__main__":
main()
