class Solution:
    # @param s (string)
    # @return boolean
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():  # Save only alphabetic characters
                res += i.lower()

        return res == res[::-1]

# output (코드 제출시 해당 코드는 삭제)
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))