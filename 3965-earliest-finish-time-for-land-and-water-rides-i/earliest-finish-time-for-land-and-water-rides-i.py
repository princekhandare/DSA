class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n = len(landStartTime)
        m = len(waterStartTime)

        ans = float('inf')

        # land -> water
        for i in range(n):
            land_end = landStartTime[i] + landDuration[i]
            for j in range(m):
                start = max(land_end, waterStartTime[j])
                ans = min(ans, start + waterDuration[j])

        # water -> land
        for j in range(m):
            water_end = waterStartTime[j] + waterDuration[j]
            for i in range(n):
                start = max(water_end, landStartTime[i])
                ans = min(ans, start + landDuration[i])

        return ans