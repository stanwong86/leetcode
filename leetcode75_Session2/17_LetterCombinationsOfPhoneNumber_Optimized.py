class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
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

        output = []

        def dfs(digits, baseLetters):
            if not digits:
                output.append(baseLetters)
                return

            digitLetters  = digitsToLetters[int(digits[0])]
            
            for dL in digitLetters:
                dfs(digits[1:], baseLetters + dL)
        
        dfs(digits, "")
        return output