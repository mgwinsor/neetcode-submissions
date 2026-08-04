class Solution:
    def isValid(self, s: str) -> bool:
        valid_stack = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                valid_stack.append(p)
                continue
            
            if not valid_stack:
                return False

            last = valid_stack[-1]
            if p == ')':
                if last == '(':
                    valid_stack.pop(-1)
                else:
                    return False

            if p == ']':
                if last == '[':
                    valid_stack.pop(-1)
                else:
                    return False
            
            if p == '}':
                if last == '{':
                    valid_stack.pop(-1)
                else:
                    return False 
        
        return not valid_stack