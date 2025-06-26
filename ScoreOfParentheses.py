class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Start with a 0 to accumulate the final score

        for char in s:
            if char == '(':
                stack.append(0)  # Start a new score context
            else:
                val = stack.pop()
                if val == 0:
                    stack[-1] += 1  # "()" → score 1
                else:
                    stack[-1] += 2 * val  # "(A)" → 2 * A

        return stack[0]
