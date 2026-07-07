from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_dict = {}

        for string in strs:
            key = tuple(sorted(Counter(string).items()))

            if key in my_dict:
                my_dict[key].append(string)
            else:
                my_dict[key] = [string]
        
        output = []

        for values in my_dict.values():
            output.append(values)
            
        return output