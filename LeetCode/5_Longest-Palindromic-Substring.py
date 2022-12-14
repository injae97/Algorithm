class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Palindrome distinction & Two-Pointer Expansion
        def expand(left: int, right: int) -> str:
            # set boundaries (e.g b==b, a==a)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right] # Save Palindrom Value (e.g: s[0:3] -> bab)

        # Exception Handling
        if len(s) < 2 or s == s[::-1]:
            return s

        # Sliding Window (Continue to the right)
        res = ''
        for i in range(0, len(s) - 1):
            res = max(res,
                      expand(i, i + 1), # even (짝수)
                      expand(i, i + 2), # odd (홀수)
                      key=len)
        return res

s = "babad"
print(Solution().longestPalindrome(s))