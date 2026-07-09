from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = {}
        
        for string in strs:
            # gets the keys and values from dict ie a:1, b:0 .... 
            key = tuple(sorted(Counter(string).items()))
            
            print(key)
            
            if key in my_dict:
                my_dict[key].append(string)
            
            else:
                my_dict[key] = [string]

        result = []

        for value in my_dict.values():
            result.append(value)

        return result
            

