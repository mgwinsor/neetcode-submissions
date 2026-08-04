class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        other_words = strs[1:]

        common_prefix = ""
        for i in range(len(first_word)):
            found_diff = False
            for j in range(len(other_words)):
                next_word = other_words[j]
                if i >= len(next_word) or next_word[i] != first_word[i]:
                    found_diff = True
            if found_diff:
                break
            common_prefix += first_word[i]
                
        return common_prefix