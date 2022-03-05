def encode(mess, key):
    acc = ""
    for i in mess:
        och = ord(i)
        shift = och + key
        nch = chr(shift)
        acc = acc + nch
    return acc


def encode_better(pltxt, cypherwd):
    acc = ""
    for i in range(len(pltxt)):
        charnum = (ord(pltxt[i])) - 65
        key = (ord(cypherwd[i % len(cypherwd)])) - 65
        shift = (charnum + key) % 58
        shift_2 = shift + 65
        newcha = chr(shift_2)
        acc = acc + newcha
    return acc

