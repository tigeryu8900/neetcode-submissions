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
            u = stack[-1]
            if not adj[u]:
                ans.append(stack.pop())
            else:
                stack.append(adj[u].pop())

        ans.reverse()
        return ans
