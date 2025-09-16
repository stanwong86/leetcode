class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToLetters = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        def dfs(digits, baseLetters):
            if not digits:
                return baseLetters

            digit = digits[0]
            digitLetters  = digitsToLetters[int(digit)]

            res = []
            newBase = []
            if not baseLetters:
                newBase = list(digitLetters)
            else:
                for bL in baseLetters:
                    for dL in digitLetters:
                        newBase.append(bL + dL)
            
            return dfs(digits[1:], newBase)
        
        if len(digits) >= 1:
            return dfs(digits, [])
        else:
            return []
        