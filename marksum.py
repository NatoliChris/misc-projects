#!/usr/bin/env python3
import sys

marks_list = []

def mark_sum():
    while(True):
        print("Please input your marks")
        marks = 0.0
        for line in sys.stdin:
            line = line.replace("`", "1")
            if(len(line) == 1):
                print('Sum: {0:.2f}'.format(marks))
                break
            try:
                if(len(line) == 4 and '.' not in line and 'q' not in line):
                    marks += float(line)/10
                elif('q' in line):
                    marks += float(line.replace('q',''))/10
                else:
                    marks += float(line)
            except:
                print("")

def average_marks():
    print("Please input your marks")
    for line in sys.stdin:
        if(len(line) == 1):
            print('AVG: {0:.2f}'.format((sum(marks_list)/ float(len(marks_list)))))
            sys.exit(0)
        marks_list.append(float(line))

if(__name__ == '__main__'):
    if(len(sys.argv) == 1):
        mark_sum()
    elif(sys.argv[1] == '-a'):
        average_marks()

