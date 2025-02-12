def removeDigit(number: str, digit: str) -> str:
    new_num = ""
    for i in range(len(number)):
        if number[i] == digit:
            cur_num = number[:i] + number[i+1:]
            new_num = max(cur_num, new_num)
    return new_num





number = "123"
digit = "3"
print(removeDigit(number, digit))