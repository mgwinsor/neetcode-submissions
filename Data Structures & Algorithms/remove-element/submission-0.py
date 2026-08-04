class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_indexes = []
        for i in range(len(nums)-1, -1, -1):
            if val == nums[i]:
                val_indexes.append(i)
        
        for idx in val_indexes:
            nums.pop(idx)
        
        return len(nums)