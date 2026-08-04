class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > threshold:
                return num