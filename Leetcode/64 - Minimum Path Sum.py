class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float('inf')
            memo[(i, j)] = grid[i][j] + min(dfs(i-1, j), dfs(i, j-1))
            return memo[(i, j)]
        
        return dfs(m-1, n-1)
