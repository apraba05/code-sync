class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        max_len = 0
        left = 0

        for right in range(len(s)):