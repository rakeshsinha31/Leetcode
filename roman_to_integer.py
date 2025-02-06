def romanToInt(s: str) -> int:
    mapp = {'I':1, "II": 2, "III": 3, "IV": 4, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}
    res = 0
    for i in range(len(s)):
        if i+1 < len(s) and mapp[s[i]] < mapp[s[i+1]]:
            res -= mapp[s[i]]
        else:
             res += mapp[s[i]]
    return res



s = "CMXCVIII"
ss = romanToInt(s)
print(ss)