class Solution(object):
    def sequentialDigits(self, low, high):
        result=[]
        for start in range(1,10):
            nums=0
            for digit in range(start,10):
                nums=nums*10+digit
                if low<=nums<=high:
                    result.append(nums)
        result.sort()
        return result
        