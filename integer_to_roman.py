def integer_to_roman(number):
    ROMAN_NUMERAL_TABLE = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100),  ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),
    ("IX", 9),   ("V", 5),    ("IV", 4),
    ("I", 1)]
    roman_numerals = []
    for numeral, value in ROMAN_NUMERAL_TABLE:
    	count = number // value
    	number = number - count * value
    	#count,number = divmod(number, value)
    	print count, number
    	roman_numerals.append(numeral * count)
    return ''.join(roman_numerals)
            

print integer_to_roman(49)