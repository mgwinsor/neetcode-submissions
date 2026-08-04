class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for element in operations:
            try:
                score = int(element)
                stack.append(score)
            except:
                pass

            if element == "+":
                new_score = stack[-1] + stack[-2]
                stack.append(new_score)
            
            if element == "C":
                stack.pop()

            if element == "D":
                new_score = 2 * stack[-1]
                stack.append(new_score)

        return sum(stack)