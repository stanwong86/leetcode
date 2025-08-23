class Solution:
    def compress(self, chars: List[str]) -> int:
        # if dupe, pop it, increase count x
        # single char - end 
        # multiple char - end
        # last char -end

        charCount = 1
        prev = chars[0]

        i = 1
        while i < len(chars):
            if chars[i] == prev:
                chars.pop(i)
                charCount += 1
                # new i
            else:
                if charCount > 1:
                    for c in str(charCount):
                        chars.insert(i, c)
                        i += 1
                    
                prev = chars[i]
                charCount = 1
                i += 1
                
        if charCount > 1:
            for c in str(charCount):
                chars.append(c)
        return len(chars)
