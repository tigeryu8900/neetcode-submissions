import sortedcontainers


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for u, v in tickets:
            adj[u].append(v)

        stack = ["JFK"]
        ans = []

        while stack:
            if adj[u := stack[-1]]:
                stack.append(adj[u].pop())
            else:
                ans.append(stack.pop())

        ans.reverse()
        return ans
