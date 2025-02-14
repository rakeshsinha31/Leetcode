def max_area(height: list) -> int:
    l = 0
    r = len(height) -1
    area = 0

    while r > l:
        area = max(area, (r-l) * min(height[l], height[r]))
        if height[r] > height[l]:
            l += 1
        else:
            r-= 1
    return area
        
height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))