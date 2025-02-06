def canConstruct(ransomNote: str, magazine: str) -> bool:
    count_ransom = {}
    mag_map = {}
    for i in ransomNote:
        if i not in count_ransom:
            count_ransom[i] = 1
        else:
            count_ransom[i]  = count_ransom.get(i) + 1
    for i in count_ransom:
        if i in magazine and (magazine.count(i) >= count_ransom[i]):
            found = True
        else:
            return False
    return found

s1 = "bg"
s2= "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(canConstruct(s1, s2))