def number_of_palindroms(s):
        possble_subs = []
        ss=''
        for i in range(len(s)):
            ss += s[i]
            possble_subs.append(ss)
        d = {}
        for i in possble_subs:
            if i[len(i)-1::-1] == i and len(i) >1:
                if len(i) not in d:
                    d[len(i)] = i
        print d
        if d.values():
            k = max(d.keys())
            return d[k]
        else:
            return ''

number_of_palindroms("babad")