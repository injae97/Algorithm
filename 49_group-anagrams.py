import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            """
            sorted(word)  # ['a', 'e', 't']
            ''.join(sorted(word)) # aet
            [''.join(sorted(word))] # ['aet']            
            """
            # 문자 정렬 후 딕셔너리 추가
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())

# Input On LeetCode
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
