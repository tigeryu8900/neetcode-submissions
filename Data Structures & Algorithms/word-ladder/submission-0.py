import functools

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        Q = deque(((1, beginWord),))
        while Q:
            d, u = Q.popleft()
            if u == endWord:
                return d
            i = 0
            while i < len(wordList):
                v = wordList[i]
                if sum(a != b for a, b in zip(u, v)) == 1:
                    Q.append((d + 1, v))
                    wordList[i] = wordList[-1]
                    wordList.pop()
                else:
                    i += 1
        return 0
