class Solution(object):
    def leftRightDifference(self, nums):
         total=sum(nums)
         leftsum=0
         anser=[]

         for num in nums:
            rightsum=total-leftsum-num
            anser.append(abs(leftsum-rightsum))
            leftsum+=num

     
         return anser 

        