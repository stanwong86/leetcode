'''
I originally tried a brute force with 2 pointes to loop through every element, but that was too slow.

This second solution was optimized a little better it doesn't need to loop through every element again. Just the ones that have no mapped values.

If temperature always decreases, then it would be O(n**2).
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        unmapped_temps = defaultdict(list)
    
        for l in range(len(temperatures)):
            temp = temperatures[l]
            temps_to_remove = []
            for unmapped_temp, indexes in unmapped_temps.items():
                if unmapped_temp < temp:
                    for i in indexes:
                        temperatures[i] = l-i
                    temps_to_remove.append(unmapped_temp)
            
            for temp_to_remove in temps_to_remove:
                del unmapped_temps[temp_to_remove]
            
            unmapped_temps[temp].append(l)

        for indexes in unmapped_temps.values():
            for i in indexes:
                temperatures[i] = 0
        
        return temperatures