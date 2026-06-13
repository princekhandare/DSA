class Solution(object):
    def mapWordWeights(self, words, weights):
        answer = ""

        for word in words:
            total = 0

            for ch in word:
                index = ord(ch) - ord('a')
                total += weights[index]

            modulo = total % 26
            mapped_char = chr(ord('z') - modulo)
            answer += mapped_char

        return answer
        