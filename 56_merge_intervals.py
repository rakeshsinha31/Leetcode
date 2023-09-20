def merge_intervals(intervals):
    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]
    for start, end in intervals[1:]:
        print(output)
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(end, last_end)
        else:
            output.append([start, end])
    return output


inp = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(inp))
