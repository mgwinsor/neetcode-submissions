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
                operand_1 = numbers.pop()
                operand_2 = numbers.pop()
                numbers.append(op(operand_1, operand_2))
            else:
                numbers.append(int(token))
        return numbers[0]