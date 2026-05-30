class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False

                popped = stack.pop()
                
                if i == ')' and popped != '(':
                    return False
                elif i == ']' and popped != '[':
                    return False
                elif i == '}' and popped != '{':
                    return False
        
        return not stack