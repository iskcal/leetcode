def isPalindrome(x):
    if x < 0:
        return False
    else:
        p = []
        while x > 0:
            p.append(x%10)
            x = x // 10
        
        for i in range(len(p)//2):
            if p[i] != p[len(p)-1-i]:
                return False
        return True

if __name__ == '__main__':
    check = isPalindrome(1331)
    print(check)