class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        result = []
        
        for i in range(len(searchWord)):
            temp = []
            for product in products:
                if product.startswith(searchWord[:i+1]):
                    temp.append(product)
            result.append(temp[:3])
        return result