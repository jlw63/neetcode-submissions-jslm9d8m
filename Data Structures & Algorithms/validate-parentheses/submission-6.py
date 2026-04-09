class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                if not stack:
                    return False
                check = stack.pop()
                if check != "[":
                    return False
            elif s[i] == ")":
                if not stack:
                    return False
                check = stack.pop()
                if check != "(":
                    return False
            elif s[i] == "}":
                if not stack:
                    return False
                check = stack.pop()
                if check != "{":
                    return False
            else:
                stack.append(s[i])
        if not stack:
            return True
        return False
