def longestCommonPrefix(strs: list) -> str:
    prefix = strs[0]

    for i in range(len(prefix)):
        for word in strs:
            if word[i] != prefix[i] or len(word) == i:
                return prefix[:i]
    return prefix




strs = ["fl","flow","flight"]
l = longestCommonPrefix(strs)
print(l)