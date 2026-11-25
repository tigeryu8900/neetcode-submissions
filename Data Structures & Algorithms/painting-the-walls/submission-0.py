class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n = len(cost)
        curr = [0] * n
        prev = [float("inf")] * n
        for c, t in zip(cost, time):
            for j in range(n):
                curr[j] = min(
                    c + prev[j - t - 1] if j > t else c,
                    prev[j],
                )
            prev, curr = curr, prev
        return prev[-1]
