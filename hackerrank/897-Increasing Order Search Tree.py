class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      values = []
      def inorder(node):
        if not node:
          return
        inorder(node.left)
        values.append(node.val)
        inorder(node.right)
      
      dummy = TreeNode(-1)
      current = dummy
      for v in values:
        current.right = TreeNode(v)
        current = current.right
      
      return dummy.right
