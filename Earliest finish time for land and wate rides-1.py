class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        ans = float('inf')

        
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_begin = max(land_finish, waterStartTime[j])
                ans = min(ans, water_begin + waterDuration[j])

       
        for i in range(len(waterStartTime)):
            water_finish = waterStartTime[i] + waterDuration[i]

            for j in range(len(landStartTime)):
                land_begin = max(water_finish, landStartTime[j])
                ans = min(ans, land_begin + landDuration[j])

        return ans
        
