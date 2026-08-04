class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_in_s = self.count_letters(s)
        letters_in_t = self.count_letters(t)
        return letters_in_s == letters_in_t

    def count_letters(self, word: str) -> dict[str, int]:
        letter_count = {}
        for char in word:
            letter_count[char] = letter_count.get(char, 0) + 1
        return letter_count