def isPalindrome(s) -> bool:
    s = s.replace(" ","")
    l=0
    r=len(s)-1
    print(s)
    while r >= l:
        print(r, l)
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

s="a, man a plan a canal panama"
# print(isPalindrome(s))


def isPalindrome2(s) -> bool:
    s1=""
    for i in s:
        if i.isalnum():
            s+= i.lower()

    l=0
    r=len(s1)-1
    while r >= l:
        if s1[l] == s1[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

s="A man, a plan, a canal: Panama"
print(isPalindrome2(s))