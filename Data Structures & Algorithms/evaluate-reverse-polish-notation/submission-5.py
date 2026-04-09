class Solution:
    def evalRPN(self, token: List[str]) -> int:
        stack = []
        for i in range(len(token)):
            if token[i] == "+":
                v1 = stack[-1]
                stack.pop()
                v2 = stack[-1]
                stack.pop()
                result = v1 + v2
                stack.append(result)
            elif token[i] == "-":
                v1 = stack[-1]
                stack.pop()
                v2 = stack[-1]
                stack.pop()
                result = v2 - v1
                stack.append(result)
            elif token[i] == "/":
                v1 = stack[-1]
                stack.pop()
                v2 = stack[-1]
                stack.pop()
                result = int(v2 / v1)
                stack.append(result)
            elif token[i] == "*":
                v1 = stack[-1]
                stack.pop()
                v2 = stack[-1]
                stack.pop()
                result = v1 * v2
                stack.append(result)
            else:
                stack.append(int(token[i]))
        return int(stack[-1])
        