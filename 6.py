def reverse( x):
    x = str(x)
    if len(x) == 0:
        return 0
    if '-' in x:
        x = x.replace('-','')
        print x
        x = '-' + x[len(x)-1 : : -1]
        return int(x)
    else:
        return int( x[len(x)-1 : : -1])
print reverse(-321)