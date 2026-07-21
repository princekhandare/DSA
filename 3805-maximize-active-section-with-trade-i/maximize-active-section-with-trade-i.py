class Solution:
    def maxActiveSectionsAfterTrade(self, s):
        ones = s.count('1')
        t = '1' + s + '1'

        groups = []
        i = 0

        while i < len(t):
            j = i

            while j < len(t) and t[j] == t[i]:
                j += 1

            groups.append((t[i], j - i))
            i = j

        answer = ones

        for i in range(1, len(groups) - 1):
            if groups[i][0] == '1':
                if groups[i - 1][0] == '0' and groups[i + 1][0] == '0':
                    answer = max(
                        answer,
                        ones + groups[i - 1][1] + groups[i + 1][1]
                    )

        return answer
        