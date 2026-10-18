class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = [] 
        ope = ["/", "+", "-", "*"]
        for t in tokens:
            if t not in ope:
                stack.append(int(t))
            else:
                right_n = stack.pop()
                left_n = stack.pop()
                if t == "+":
                    stack.append(left_n + right_n)
                if t == "/":
                    stack.append(int(left_n / right_n))
                if t == "*":
                    stack.append(left_n * right_n)
                if t == "-":
                    stack.append(left_n - right_n)
        return stack[0]