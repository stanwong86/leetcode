def smallestStringWithSwaps(s, pairs) -> str:
        
    s = list(s)
    while 1:
        
        swapped = False
        for i, j in pairs:
            
            if s[i] > s[j]:
                print(i, j, s[i], s[j], ''.join(s))
                print('before', s)
                s[i], s[j] = s[j], s[i]
                print('after', s)
                swapped = True
                break
                
        if not swapped:
            break
            
    return ''.join(s)

smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]])