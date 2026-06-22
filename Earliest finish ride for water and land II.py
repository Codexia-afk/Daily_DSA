class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        def solve(start1, dur1, start2, dur2):
            rides = sorted(zip(start2, dur2))

            starts = [x[0] for x in rides]

            n = len(rides)

            # suffix minimum of (start + duration)
            suffix = [0] * n
            suffix[-1] = rides[-1][0] + rides[-1][1]

            for i in range(n - 2, -1, -1):
                suffix[i] = min(suffix[i + 1],
                                rides[i][0] + rides[i][1])

            # prefix minimum of duration
            prefix = [0] * n
            prefix[0] = rides[0][1]

            for i in range(1, n):
                prefix[i] = min(prefix[i - 1], rides[i][1])

            ans = float("inf")

            for s, d in zip(start1, dur1):
                finish = s + d

                idx = bisect_left(starts, finish)

                # wait for next ride
                if idx < n:
                    ans = min(ans, suffix[idx])

                # ride already opened
                if idx > 0:
                    ans = min(ans, finish + prefix[idx - 1])

            return ans

        return min(
            solve(landStartTime, landDuration,
                  waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration,
                  landStartTime, landDuration)
        )
        
