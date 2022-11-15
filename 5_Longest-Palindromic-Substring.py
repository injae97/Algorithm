class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Palindrome distinction & Two-Pointer Expansion
        def expand(left: int, right: int) -> str:
            print("left:",left)
            print("s[left]:", s[left])
            print("right:", right)
            print("right:", s[right])

            # set boundaries
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        # Exception Handling
        if len(s) < 2 or s == s[::-1]:
            return s

        res = ''
        for i in range(0, len(s) - 1):
            res = max(res,
                      expand(i, i + 1), # even (짝수)
                      expand(i, i + 2), # odd (홀수)
                      key=len)
        return res

s = "babad"
print(Solution().longestPalindrome(s))