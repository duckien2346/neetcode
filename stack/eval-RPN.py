from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ['+','-','*','/']:
                stack.append(int(t))
                continue
            right = stack.pop()
            left = stack.pop()
            match t:
                case '+':
                    stack.append(left + right)
                case '-':
                    stack.append(left - right)
                case '*':
                    stack.append(left * right)
                case '/':
                    stack.append(int(left / right))
                case _:
                    return stack.pop()
        return stack.pop()

s = ["1","2","+","3","*","4","-"]
s = ["4","13","5","/","+"]
resolve = Solution()
result = resolve.evalRPN(s)
print(result)
