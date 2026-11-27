class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        idx = {x: i for i, x in enumerate(sorted(set(obstacles)))}
        bit = [0] * len(idx)
        ans = []
        for x in obstacles:
            cur = 0
            i = idx[x]
            while i >= 0:
                cur = max(cur, bit[i])
                i = (i & (i + 1)) - 1
            cur += 1
            ans.append(cur)
            i = idx[x]
            while i < len(bit):
                cur = bit[i] = max(cur, bit[i])
                i |= i + 1
        return ans
