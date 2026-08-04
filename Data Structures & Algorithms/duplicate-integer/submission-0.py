class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if count.get(num) == None:
                count[num] = 1
            else:
                return True
        return False