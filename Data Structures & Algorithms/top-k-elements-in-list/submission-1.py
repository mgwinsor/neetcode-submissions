class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i, n in enumerate(nums):
            counter[n] = counter.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for element, frequency in counter.items():
            buckets[frequency].append(element)
        
        top_freq = []
        for i in range(len(buckets) -1, -1, -1):
            for element in buckets[i]:
                top_freq.append(element)
                if len(top_freq) >= k:
                    return top_freq
        return top_freq