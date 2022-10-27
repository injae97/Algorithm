class Solution:
    # @param s (string)
    # @return boolean
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum(): # [a-zA-Z0-9]
                res += i.lower()

        return res == res[::-1]

# input
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))