import re, time

file = input("enter file name: ")
if len(file) < 1:
    file = "mbox-short.txt"
open_f = open(file)

pattern = re.compile(r'\S+[.]\S+[.]\S+[.]')

for line in open_f:
    if pattern.search(line):
        i = pattern.search(line)
        m = i.group()
        print(m)
