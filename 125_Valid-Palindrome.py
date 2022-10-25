class Solution:
    # @param s (string)
    # @return boolean
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():  # Save only alphabetic characters
                res += i.lower()

        return res == res[::-1]