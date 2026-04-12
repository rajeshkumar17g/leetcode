class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        G = [[] for i in range(n)]
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        res = [0]

        def dfs(i, f = -1):
            score = []
            for j in G[i]:
                if j == f: continue
                score.append(dfs(j, i))
            if not score:
                return cost[i]
            ma = max(score)
            res[0] += sum(ma - v > 0 for v in score)
            return ma + cost[i]

        dfs(0)
        return res[0]