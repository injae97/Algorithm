# Best Solution - two pointer (524ms)
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        :type s: List[str]
        :rtype : List[str]
        """
        l,r = 0, len(s)-1
        while l < r :
            s[l], s[r] = s[r], s[l] # swap
            l += 1
            r -= 1


# Input On LeetCode
TC_1 =  ["h","e","l","l","o"]
TC_2 =  ["H","a","n","n","a","h"]
print(Solution().reverseString(TC_1))
print(Solution().reverseString(TC_2))


# list-reverse Solution (669ms)
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        :type s: List[str]
        :rtype : List[str]
        """
        s.reverse()


# reverse-trick Solution (265ms)
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        :type s: List[str]
        :rtype : List[str]
        """
        s[:] = s[::-1] # trick -> s[:]