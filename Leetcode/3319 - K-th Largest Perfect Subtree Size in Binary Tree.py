class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return 0, True

            left_s, left_perf = dfs(node.left)
            right_s, right_perf = dfs(node.right)

            is_perf = left_perf and right_perf and left_s == right_s
            size = left_s + right_s + 1
            
            if is_perf:
                perf_s.append(size)

            return size, is_perf

        perf_s = []
        dfs(root)
        perf_s.sort(reverse = True)

        return perf_s[k - 1] if k <= len(perf_s) else -1
