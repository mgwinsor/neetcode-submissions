class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operators = {
            "+": lambda a, b: b + a,
            "-": lambda a, b: b - a,
            "*": lambda a, b: b * a,
            "/": lambda a, b: int(b / a)
        }
        for token in tokens:
            if token in operators:
                op = operators[token]
                res = op(numbers.pop(), numbers.pop())
                numbers.append(res)
            else:
                numbers.append(int(token))
        return numbers[0]