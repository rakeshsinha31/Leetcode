"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator."""


def square_root(num):
    l, r = 0, num // 2
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == num:
            return mid
        if mid * mid > num:
            r = mid - 1
        else:
            l = mid + 1
    return mid - 1


print(square_root(18))
