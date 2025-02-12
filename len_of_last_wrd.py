def lengthOfLastWord( s: str) -> int:
    c = 0
    for i in reversed(s):
        print(i)
        if i !="":
            c+= 1
        else:
            break
    return c

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
# return(len(s.split()[-1]))