def numberToWords(number):
    mapp = [
        (100, "Hundred"),
        (20, "twenty"),
        (19, "Ninteen"),
        (18, "Eighteen"),
        (17, "Seventeen"),
        (16, "Sixteen"),
        (15, "fifteen"),
        (14, "Fourteen"),
        (13, "Thriteen"),
        (12, "twelve"),
        (11, "eleven"),
        (10, "ten"),
        (9, "nine"),
        (8, "eight"),
        (7, "seven"),
        (6, "six"),
        (5, "five"),
        (4, "four"),
        (3, "three"),
        (2, "two"),
        (1, "one"),
    ]
    word = ""
    for value, wd in mapp:
        if value <= number:
            count = number // value
            number = number * count - value
            word = 
            print(number, count, wd)


numberToWords(345)
