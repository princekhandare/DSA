class Solution(object):
    def shiftGrid(self, grid, k):
        m=len(grid)
        n=len(grid[0])
        total=m*n
        arr=[]
        for row in grid:
            arr.extend(row)
        k=k%total;
        arr = arr[-k:] + arr[:-k]
        result=[]
        for i in range(0,total,n):
            result.append(arr[i:i+n])

        return result