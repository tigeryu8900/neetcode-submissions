import bisect


class Solution:
    key = lambda x: (x[0], -x[2], -x[1])

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        t = sorted(zip(startTime, endTime, profit), key=Solution.key)
        dp = [0] * (len(t) + 1)
        dp[-2] = t[-1][2]
        for i in range(len(t) - 2, -1, -1):
            s, e, p = t[i]
            dp[i] = max(
                dp[i + 1],
                p
                + dp[
                    bisect.bisect_left(
                        t, (e, float("-inf"), float("-inf")), lo=i + 1, key=Solution.key
                    )
                ],
            )
        return dp[0]
