class Solution:
    def findRotateSteps(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        vis = [[False] * (m + 1) for _ in range(n)]
        vis[0][0] = True
        q = [(0, 0)]
        step = 0
        while True:
            tmp = q
            q = []
            for i, j in tmp:
                if j == m:
                    return step
                if s[i] == t[j]:
                    if not vis[i][j + 1]:
                        vis[i][j + 1] = True
                        q.append((i, j + 1))
                    continue
                for i2 in (i - 1) % n, (i + 1) % n:
                    if not vis[i2][j]:
                        vis[i2][j] = True
                        q.append((i2, j))
            step += 1

