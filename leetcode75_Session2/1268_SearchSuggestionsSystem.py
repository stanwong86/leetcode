class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        wordDict = {}
        for product in products:
            for i in range(len(product)):
                subString = product[:i+1]
                if subString not in wordDict:
                    wordDict[subString] = []
                
                # Needed to sort words too
                words = wordDict[subString]
                for i in range(len(words)):
                    if product <= words[i]:
                        wordDict[subString].insert(i, product)
                        break
                else:
                    wordDict[subString].append(product)

        res = []
        for i in range(len(searchWord)):
            subString = searchWord[:i+1]
            if subString in wordDict:
                res.append(wordDict[subString][:3])
            else:
                res.append([])
        
        return res
