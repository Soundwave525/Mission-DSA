class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        def buildBalanced(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(values[mid])
            node.left = buildBalanced(left, mid  - 1)
            node.right = buildBalanced(mid + 1, right)
            return node

        return buildBalanced(0, len(values) - 1)
