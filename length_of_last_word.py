def lengthOfLastWord(s: str) -> int:
    #return(len(s.split()[-1]))
    
    res = 0
    for i in s:
        if i !="":
            sum = 0
            for j in i:
                sum += 1
            
            res = max(res, sum)
            # print(res)
    # print(res)
    return res

s = "luffy is still joyboy"
print(lengthOfLastWord(s))