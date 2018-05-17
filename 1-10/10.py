class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        se = len(s)-1
        pe = len(p)-1

        while pe > 0 and se > 0 and p[pe] != '*':  # 尾部判断提高效率
            if p[pe] != '.' and p[pe] != s[se]:
                return False
            else:
                se -= 1
                pe -= 1

        return self.checkMatch(s[:se+1], p[:pe+1], 0, 0)

    def checkMatch(self, s, p, si, pi):
        if len(p[pi:]) == 0: # 模式串为空
            return len(s[si:]) == 0
        if len(s[si:]) == 0: # 被检查串为空
            return len(p[pi:]) == 0 or (len(p[pi:])%2 == 0 and p[pi+1::2] == ''.join(['*' for i in range(len(p[pi:])//2)]))

        # 三种情况
        if (len(p[pi:]) > 1) and (p[pi+1] == '*'):
            if self.checkMatch(s, p, si, pi+2): # 模式串后面紧跟*，此时判断略过该字符
                return True
            else: # 判断匹配至少一次的情形
                return (s[si] == p[pi] or p[pi] == '.') and self.checkMatch(s, p, si+1, pi)
        else: # 没有*条件，要求必须匹配
            return (p[pi] == s[si] or p[pi] == '.') and self.checkMatch(s, p, si+1, pi+1)
    
if __name__ == '__main__':
    a = Solution()
    result = a.isMatch("a", "b..")
    print(result)
    
