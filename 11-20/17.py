def letterCombinations(digits):
    alphabet = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    return letterCombinationsCore(digits, alphabet)

def letterCombinationsCore(digits, alphabet):
    if len(digits) == 0:
        return []
    elif len(digits) == 1:
        return [c for c in alphabet[digits[0]]]
    else:
        return [c1+c2 for c1 in letterCombinationsCore(digits[0:len(digits)//2], alphabet) for c2 in letterCombinationsCore(digits[len(digits)//2:], alphabet)]

if __name__ == '__main__':
    print(letterCombinations('23'))