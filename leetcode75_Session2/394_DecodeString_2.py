class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        numCount = 0
        currStr = ''
        for char in s:
            if char.isdigit():
                numCount = 10 * numCount + int(char)
            elif char == '[':
                stack.append(currStr)
                stack.append(numCount)
                currStr = ''
                numCount = 0
            elif char == ']':
                prevNum = stack.pop()
                prevStr = stack.pop()

                numCount = 0
                currStr = prevStr + currStr * prevNum
            else:
                currStr += char
        return currStr