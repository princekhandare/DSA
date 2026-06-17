class Solution(object):
    def processStr(self, s, k):
        n = len(s)
        length = [0] * (n + 1)

        # Forward pass: store only lengths
        for i in range(n):
            if 'a' <= s[i] <= 'z':
                length[i + 1] = length[i] + 1
            elif s[i] == '*':
                length[i + 1] = max(0, length[i] - 1)
            elif s[i] == '#':
                length[i + 1] = length[i] * 2
            else:  # '%'
                length[i + 1] = length[i]

        if k >= length[n]:
            return '.'

        # Backward pass: trace the index
        for i in range(n - 1, -1, -1):
            ch = s[i]

            if 'a' <= ch <= 'z':
                if k == length[i]:
                    return ch

            elif ch == '*':
                # Before '*', one extra character existed at the end.
                pass

            elif ch == '#':
                half = length[i]
                if k >= half:
                    k -= half

            elif ch == '%':
                k = length[i] - 1 - k

        return '.'