def reverse(x):
    r = 0
    t = x if x>=0 else -x

    while t > 0:
        r = r * 10 + t % 10
        t = t // 10
        if r * 10 > 2 ** 31:
            r = 0
            break
    
    r = r if x >=0 else -r
    return r

if __name__ == '__main__':
    tt = reverse(123456789)