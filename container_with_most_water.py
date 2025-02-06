def container_with_most_water(height: list) -> int:
    l =0 
    r = len(height)-1
    area = 0
    while r>l:
        area = max(area,  (r-1) * min(height[l], height[r]))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return area


height = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water(height))