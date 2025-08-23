'''
Use a separate writePointer
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        writePointer = 0
        charCount = 1
        for i in range(1, len(chars)+1):
            if (i < len(chars) and chars[i] == chars[i-1]):
                charCount += 1
            else:
                chars[writePointer] = chars[i-1]
                writePointer += 1

                if charCount > 1:
                    for c in str(charCount):
                        chars[writePointer] = c
                        writePointer += 1
                
                    charCount = 1
        
        while writePointer < len(chars):
            chars.pop(writePointer)
        return writePointer