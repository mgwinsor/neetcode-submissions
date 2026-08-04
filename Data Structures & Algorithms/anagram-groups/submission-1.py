class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = self.get_key(word)
            groups[key].append(word)
        return list(groups.values())

    def get_key(self, word: str) -> Tuple:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        return tuple(count)