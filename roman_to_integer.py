#def roman_to_integer(input_roman):
    #roman_mapping = {'I':1, 'V':5, 'X':10, 'L':50,'C':100,'D':500,'M':1000}
	# decimal = roman_mapping[input_roman[-1]]
	# print decimal
	# for i in range(len(input_roman)-1, -1, -1):
	# 	if roman_mapping[input_roman[i]] >= roman_mapping[input_roman[i-1]]:
	# 		decimal = decimal + roman_mapping[input_roman[i]]
	# 		print roman_mapping[input_roman[i]], decimal
	# 	else:
	# 		decimal = decimal - roman_mapping[input_roman[i]]
	# 		roman_mapping[input_roman[i]], decimal
	# return decimal

def romanToInt(s):
    numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
    decimal = 0
    for i in xrange(len(s)):
        if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
            decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
        else:
            decimal += numeral_map[s[i]]
    return decimal


print(romanToInt('IX'))
