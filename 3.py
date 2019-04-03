def lengthOfLongestSubstring(word):
    # Initially we can go as far to the left as we want
        n = len(word)
        longest = 0
        for i in range(n):
            print 'i = ', i
            seen = set()
            for j in range(i, n):
                print 'j= ',j
                if word[j] in seen: break
                seen.add(word[j])
                print  'seen= ',  seen
            longest = max(len(seen), longest)
        return longest
        

print lengthOfLongestSubstring('pwwkewr')
