class Solution:
    def permuteUnique(self, nums):
    
        def permutations(head, tail = []) -> list:
            if len(head) == 0:
                return [tail]

            perms = []
            for i in range(len(head)):

                perm = permutations(head[:i] + head[i+1:], tail + head[i:i+1])

                if perm and perm[0] not in perms:
                    perms.extend(perm)

            return perms
        return permutations(nums)



s = Solution()
r = s.permuteUnique([1,1,2])
print(r)


