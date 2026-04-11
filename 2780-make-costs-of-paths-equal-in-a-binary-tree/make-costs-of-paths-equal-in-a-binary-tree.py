class Solution:
    def minIncrements(self, n, cost):
        self.res = 0
        def dfs(i):
            if i >= len(cost): return 0
            a, b = dfs(2 * i + 1), dfs(2 * i + 2)
            self.res += abs(a - b)
            return cost[i] + max(a, b)
        dfs(0)
        return self.res