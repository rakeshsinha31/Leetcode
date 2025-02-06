def longest_valid_parantheses(s: str) -> int:
    l = r = maxx = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            l += 1
        else:
            r += 1
        if l == r:
            maxx = max(maxx, l+r)
        elif r>l:
            l = r = 0
        i+= 1
    i=r=0
    i = len(s) - 1
    while i>0:
        if s[i] == "(":
            l += 1
        else:
            r += 1
        if l==r:
            maxx = max(maxx, l+r)
        elif l>r:
            l=r=0
        i-= 1
    return(maxx)

s = "(()()()()"
num = longest_valid_parantheses(s)
print(num)