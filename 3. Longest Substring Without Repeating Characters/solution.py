class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        word_pos = {}
        max_len = 0
        curr_len = 0
        wl = 0
        i = 0
        while i < len(s):
            curr_len += 1
            if s[i] in word_pos:
                wl = max(wl, word_pos[s[i]] + 1)
                curr_len -= 1
                max_len = max(max_len, curr_len)
                curr_len = i - wl + 1
                word_pos[s[i]] = i
            word_pos[s[i]] = i
            i += 1
        max_len = max(max_len, curr_len)
        return max_len
