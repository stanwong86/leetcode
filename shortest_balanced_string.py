'''
A string is called balance when every letter occuring in the string appears in both upper and lowercase. for example, the string CATattac is balanced. Number of occurences does not matter
'''
import unittest

class Solution:
    def shortest_path(self, input1: str):
        n = len(input1)
        
        def isBalanced(s: str) -> bool:
            letters = set(s)
            for ch in letters:
                if ch.isalpha():
                    if ch.lower() not in letters or ch.upper() not in letters:
                        return False
            return True

        for size in range(n, 1, -1):
            for i in range(n):
                if i + size <= n:
                    substring = input1[i:i+size]
                    # print(f'size: {size}, i: {i}, substring: {substring}')
                    if isBalanced(substring):
                        return len(substring)
        return 0


class MyTests(unittest.TestCase):
    s = Solution()
    mainFunction = s.shortest_path

    def test1(self):
        actual = self.mainFunction('abzaaBAbz')
        self.assertEqual(actual, 5)

    def test2(self):
        actual = self.mainFunction('CabzcaBAbz')
        self.assertEqual(actual, 4)
    
    def test3(self):
        actual = self.mainFunction('CabzaBcAbz')
        self.assertEqual(actual, 0)

unittest.main()