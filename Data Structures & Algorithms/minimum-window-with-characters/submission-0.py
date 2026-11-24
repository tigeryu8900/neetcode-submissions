class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        n = len(tc)
        sc = Counter()
        m = 0
        j = 0
        ans = None
        for i, c in enumerate(s):
            sc[c] += 1
            if sc[c] == tc[c]:
                m += 1
            if m == n:
                while j < i and sc[s[j]] > tc[s[j]]:
                    sc[s[j]] -= 1
                    j += 1
                if ans is None or i + 1 - j < ans[1] - ans[0]:
                    ans = j, i + 1
        return "" if ans is None else s[ans[0]:ans[1]]
