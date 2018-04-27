def isPalindrome(x):
    if x < 0:
        return False
    else:
        t = 0
        tmp = x
        while tmp > 0:
            t = t * 10 + tmp % 10
            tmp = tmp // 10
        return t == x

if __name__ == '__main__':
    check = isPalindrome(1331)
    print(check)