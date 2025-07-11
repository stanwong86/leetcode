'''
This solution had a few trial and errors to get the return value correct.
'''

class StockSpanner:

    def __init__(self):
        self.stack = [None]
        self.temperatures = [None] 

    def next(self, price: int) -> int:
        # print('price: ', price)
        stack_i = len(self.stack)-1
        low_i = len(self.stack)
        self.temperatures.append(price)
        while stack_i >= 0:
            if not stack_i:
                if low_i != len(self.stack):
                    self.stack.append(low_i)
                    return len(self.stack) - low_i
                self.stack.append(len(self.stack))
                return 1
            elif self.temperatures[stack_i] > price:
                self.stack.append(low_i)
                return len(self.stack) - self.stack[-1]
            elif stack_i == low_i:
                stack_i -= 1
            else:
                low_i = stack_i
                stack_i = self.stack[stack_i]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


''' 
This ChatGBT solution is more concise
Keep one stack and add (price, span). You only need to keep the higher price and gobble up the lower prices because 
once a higher price is hit, we don't need to search the stack further.
'''
class StockSpanner:

    def __init__(self):
        self.stack = [] # (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop(-1)[1]

        self.stack.append((price, span))
        return span