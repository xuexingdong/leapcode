# Problem

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# Example

```text
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

```text
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

```text
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

# Solution

```python
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
   
```

时间复杂度`n`，空间复杂度`n`。

# Optimization
