def most_repeated_chars(s: str) -> str:
    count_map = {}
    for i in s:
        if not i.isdigit():
            if i not in count_map:
                count_map[i] = 1
            else:
                count_map[i] = count_map.get(i) + 1
    key = max(count_map, key=count_map.get)
    print(count_map)
    return key


s = 'aaaacs111ddddddd33rdcfd'
print(most_repeated_chars(s))