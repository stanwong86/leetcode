'''
Meta question
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if '(' == s[i]:
                stack.append(i)
            elif ')' == s[i]:
                if stack and s[stack[-1]] == '(':
                    stack.pop(-1)
                else:
                    stack.append(i)
        
        sList = list(s)
        for pIndex in stack[::-1]:
            sList.pop(pIndex)
        
        return ''.join(sList)