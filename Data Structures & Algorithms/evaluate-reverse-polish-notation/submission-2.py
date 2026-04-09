class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in range(len(tokens)):
            if tokens[n] == "+":
                value1 = stack[-1]
                stack.pop()
                value2 = stack[-1]
                stack.pop()
                result = value1 + value2
                stack.append(result)
            elif tokens[n] == "-":
                value1 = stack[-1]
                stack.pop()
                value2 = stack[-1]
                stack.pop()
                result = value2 - value1
                stack.append(result)
            elif tokens[n] == "*":
                value1 = stack[-1]
                stack.pop()
                value2 = stack[-1]
                stack.pop()
                result = value1 * value2
                stack.append(result)

            elif tokens[n] == "/":
                value1 = stack[-1]
                stack.pop()
                value2 = stack[-1]
                stack.pop()
                result = int(value2/value1)
                stack.append(result)                                          
            else:
                stack.append(int(tokens[n]))

        return stack[-1]

