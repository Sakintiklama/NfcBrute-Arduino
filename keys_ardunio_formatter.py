import os,sys


dosya = 'key.list'

satirlar = open(dosya, 'r').readlines()
for satir in satirlar:
    bisatir = satir.rstrip()
    xlebol = bisatir.lower()
    split_strings = []
    n=2
    for index in range(0, len(xlebol), n):
        split_strings.append(xlebol[index : index + n])
    bun = "{0x" + split_strings[0] + ", 0x" + split_strings[1] + ", 0x" +split_strings[2] + ", 0x" + split_strings[3] + ", 0x" + split_strings[4] + ", 0x" +split_strings[5] + "},  // " + split_strings[0].upper() + " " + split_strings[1].upper() + " " +split_strings[2].upper() + " " + split_strings[3].upper() + " " +split_strings[4].upper() + " " + split_strings[5].upper()
    
    print(bun)
