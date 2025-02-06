def int_to_roman(num: int) -> str:
    mapp =  {1: "I", 4: "IV", 
            5: "V", 9: "IX",
            10: "X", 40: "XL",50: "L", 90: "XC", 100:"C", 
            400:"CD", 500:"D", 900: "CM",1000:"M"
        }
    strr = ""

    for i in sorted(mapp.keys(), reverse=True):
        if num//i:
            count = num//i
            print(num, i, mapp[i], count)
            strr += mapp[i] * count
            num = num % i
    return strr




n = 3749
nn = int_to_roman(n)
print(nn)
# [1000, 500, 100, 50, 10, 5, 4, 3, 2, 1]