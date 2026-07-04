class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # pointer at one end points to start
        # pointer at other end points to end 
        # check they are equivalent 
        # iterate up p1
        # iterate down p2
        # when p1 exceeds p2 end

        s = s.lower()
        s =  "".join(filter(str.isalnum, s))

        p1 = 0
        p2 = len(s) - 1
         
        print(s)

        while p1 < p2:
            if s[p1] != s[p2]:
                return False 
            
            p1 += 1
            p2 -= 1
        
        return True