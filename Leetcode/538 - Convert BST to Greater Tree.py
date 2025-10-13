class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running = 0
        def reverse_inorder(node):
            nonlocal running
            if not node:
                return

            reverse_inorder(node.right)
            running += node.val
            node.val = running

            reverse_inorder(node.left)

        reverse_inorder(root)

        return root
