def longestCommonPrefix(strs: list) -> str:
    prefix = strs[0]
    for i in range(len(prefix)):
        for word in strs:
            if len(word) == i or prefix[i] != word[i]:
                return prefix[:i]
    return prefix



strs = ["flower","flow","flight"]
l = longestCommonPrefix(strs)
print(l)