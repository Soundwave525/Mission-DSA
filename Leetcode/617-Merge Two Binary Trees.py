class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
      
      if not root1:
        return root2
      
      if not root2:
        return root1
      
      new_root = Treenode(root1.val + root2.val)
      new_root.left = slef.mergeTrees(root1.left, root2.left)
      new_root.right = self.mergeTrees(root1.eight, root2.right)
      
      return new_root
