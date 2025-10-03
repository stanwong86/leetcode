class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack:
                    popped = stack.pop()
                    if c == ')' and popped != '(':
                        return False
                    elif c == '}' and popped != '{':
                        return False
                    elif c == ']' and popped != '[':
                        return False
                else:
                    return False
        return len(stack) == 0