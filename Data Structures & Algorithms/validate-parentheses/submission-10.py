class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0 or len(s) == 1:
            return False

        my_dict = {'}':'{', ']':'[', ')':'('}

        my_stack = []

        for brace in s:
            # is closing brace
            if brace in my_dict:
                # no opening braces 
                if not my_stack:
                    return False
                # if the top of the stack isnt the assosciated opening brace invalid
                elif my_stack.pop() != my_dict[brace]:
                    return False
            # otherwise brace is open so append to statcj
            else:
                my_stack.append(brace)

        if my_stack:
            return False
            
        return True



