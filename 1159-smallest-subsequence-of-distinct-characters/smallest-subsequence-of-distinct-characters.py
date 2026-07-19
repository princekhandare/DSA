class Solution(object):
    def smallestSubsequence(self, s):

        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        seen = set()

        for i in range(len(s)):
            ch = s[i]

            if ch in seen:
                continue

            while (stack and
                   stack[-1] > ch and
                   last[stack[-1]] > i):

                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)