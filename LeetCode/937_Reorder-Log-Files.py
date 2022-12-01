class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        """
        :type s: List[str]
        :rtype : List[str]
        """
        letters,digits = [], []
        for i in logs :
            # split() 공백 구분 ["dig1 8 1 5 1"] -> ['dig1', '8', '1', '5', '1']
            # 입력한 값을 공백으로 구분한 후 1번째('8') index가 숫자일 경우
            if i.split()[1].isdigit() :
                digits.append(i)

            # 입력한 값을 공백으로 구분한 후 1번째('art') index에서 문자일 경우
            else :
                letters.append(i)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(Solution().reorderLogFiles(logs))