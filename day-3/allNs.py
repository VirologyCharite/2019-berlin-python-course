def allNs_v1(string):
    nCount = 0
    for char in string:
        if char == 'N':
            nCount += 1

    if nCount == len(string):
        return True
    else:
        return False


def allNs_v2(string):
    if string.count('N') == len(string):
        return True
    else:
        return False
