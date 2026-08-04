class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total_score = 0
        stack = []

        for element in operations:
            if element == "+":
                new_score = stack[-1] + stack[-2]
                stack.append(new_score)
            elif element == "C":
                total_score -= stack[-1]
                stack.pop()
                continue
            elif element == "D":
                new_score = 2 * stack[-1]
                stack.append(new_score)
            else:
                score = int(element)
                stack.append(score)

            total_score += stack[-1]

        return total_score