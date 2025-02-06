def letter_combinations(digits: str) -> list:
    mapp = {
        2:"abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
        7: "pqrs", 8: "tuv", 9: "wxyz"
    }
    # for i in str(digits):
    #     int

    l1 = [1,2,3]
    l2 = [2,4,9]
    lk =[]

    # ll = lambda x,y: x+y
    for i in l1:
        for j in l2:
            lk.append(i*j)
    print(lk)
letter_combinations([])