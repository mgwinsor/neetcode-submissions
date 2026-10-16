class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i < len(s):
            delim_idx = s.find("#", i)
            L = int(s[i:delim_idx])
            strings.append(s[delim_idx + 1 : delim_idx + 1 + L])
            i = delim_idx + 1 + L
        return strings