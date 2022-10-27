# Best Solution (44ms)
class Solution:
    """
    :type s: str
    :rtype : bool
    """
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum(): # [a-zA-Z0-9]
                res += i.lower()

        return res == res[::-1]


# Input On LeetCode
TC_1 = "A man, a plan, a canal: Panama"
TC_2 = "race a car"
TC_3 = " "
print("TestCase #1 :", Solution().isPalindrome(TC_1))
print("TestCase #2 :", Solution().isPalindrome(TC_2))
print("TestCase #3 :", Solution().isPalindrome(TC_3))


# List Solution (324ms)
class Solution:
    """
    :type s: str
    :rtype : bool
    """
    def isPalindrome_list(self, s:str) -> bool:
        res = []
        for char in s:
            if char.isalnum():
                res.append(char.lower())

        # Time Complexity : list.pop(0) -> O(n)
        while len(res) > 1 :
            if res.pop(0) != res.pop(): # First Index != Last Index
                return False

        return True


# Deque Solution (86ms)
import collections
class Solution:
    """
    :type s: str
    :rtype : bool
    """
    def isPalindrome_deque(self, s:str) -> bool:
        strs = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # Time Complexity : deque.popleft() -> O(1)
        while len(strs) > 1:
            if strs.popleft() != strs.pop(): # Left Deque != Right Deque
                return False

        return True


# regex Solution (53ms)
import re
class Solution:
    """
    :type s: str
    :rtype : bool
    """
    def isPalindrome_regex(self, s:str) -> bool:
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]','',s)

        return s == s[::-1]


# two-pointer Solution (51ms)
class Solution:
    """
    :type s: str
    :rtype : bool
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l, r = l + 1, r - 1

        return True