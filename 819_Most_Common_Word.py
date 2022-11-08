class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """
        :type paragraph: List[str], banned: List[str]
        :rtype : str
        """


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))


