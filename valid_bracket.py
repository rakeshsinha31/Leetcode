def is_valid(s: str) -> bool:
    mapp = {"{": "}", "[": "]", "(": ")"}
    l = []
    for i in s:
        if i in mapp.keys():
            l.append(i)
        elif i in mapp.values():
            if len(l) == 0:
                return False
            char = l.pop()
            if i != mapp[char]:
                return False
    if len(l) == 0:
        return True
    else:
        return False

s = "(()())"
print(is_valid(s))