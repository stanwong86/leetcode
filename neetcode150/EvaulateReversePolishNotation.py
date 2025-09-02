class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        m = len(tokens)
        if m == 1:
            return int(tokens[0])

        res = None
        stack = []

        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                elif token == '/':
                    res = int(a / b)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[0]

