def divide(dividend, divisor):
    sign = 1 if dividend ^ divisor >= 0 else -1
    result = sign * divideCore(abs(dividend), abs(divisor))
    if result > 2**31-1 or result < -2**31:
        return 2**31-1
    else:
        return result

def divideCore(dividend, divisor):
    multiple = 1
    sum = divisor
    if divisor > dividend:
        return 0
    while sum + sum <= dividend:
        multiple += multiple
        sum += sum
    
    return multiple + divideCore(dividend-sum, divisor)

if __name__ == '__main__':
    print(divide(10,3))