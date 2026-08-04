class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if diff_map.get(difference) is not None:
                return [diff_map[difference], i]
            diff_map[nums[i]] = i

        return res