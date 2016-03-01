# http://www.pythonchallenge.com/pc/def/map.html

from string import maketrans

source = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
a = ord('a')
z = ord('z')
output = ""

for char in source:
    c = ord(char)

    if c >= a and c <= z:
        c += 2

        if c > z:
            c -= (z - a) + 1

    output += chr(c)

print output

intab = ""
outtab = ""

for c in range(a, z + 1):
    intab += chr(c)

    o = c + 2

    if o > z:
        o -= (z - a) + 1

    outtab += chr(o)

trantab = maketrans(intab, outtab)

str = "map";
print str.translate(trantab)