import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """
        :type paragraph: str, banned: List[str]
        :rtype : str
        """
        # [^\w] : 단어 문자가 아닌 문자를 공백으로 치환 후 split() 공백 구분 e.g ['B', 'o', 'b', ' '] -> ['bob']
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
            if word not in banned] # not in 을 통해 banned 값 포함X

        counts = collections.Counter(words) # counts Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
        # counts.most_common(1) --> [('ball', 2)]
        # counts.most_common(1)[0] --> ('ball', 2)
        return counts.most_common(1)[0][0] # --> ball

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))


import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """
        :type paragraph: str, banned: List[str]
        :rtype : str
        """
        # [^\w] : 단어 문자가 아닌 문자를 공백으로 치환 후 split() 공백 구분 e.g ['B', 'o', 'b', ' '] -> ['bob']
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
            if word not in banned] # not in 을 통해 banned 값 포함X

        counts = collections.defaultdict(int) # 개수를 담아두는 딕셔너리
        for word in words:
            counts[word] += 1

        return max(counts, key=counts.get)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))

