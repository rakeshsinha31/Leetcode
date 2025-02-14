def first_ocr(haystack: str, needle: str) -> int:

    for i in range(len(haystack)):
        if haystack[i: i+len(needle)] == needle:
            return i
    return -1


haystack = "myleetcode"
needle = "leet"
print(first_ocr(haystack, needle))