class Solution:
    def findMinSteps(self, ring: str, key: str) -> int:
        hs = dict()
        for i in range(len(ring)):
            if ring[i] not in hs:
                hs[ring[i]] = [i]
            else:
                hs[ring[i]].append(i)

        m, n = len(ring), len(key)
        dp = [float('inf')] * m
        for q in hs[key[0]]:
            dp[q] = min(q, m - q) + 1

        for i in range(1, n):
            if key[i] != key[i - 1]:
                for p in hs[key[i - 1]]:
                    for j in hs[key[i]]:
                        dp[j] = min(dp[j], min(abs(j - p), m - abs(j - p)) + dp[p] + 1)
                    dp[p] = float('inf')
            else:
                for j in hs[key[i]]:
                    dp[j] += 1
        return min(dp)