# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            if root.left and root.right:
                temp = root.right
                while temp.left: 
                    temp = temp.left
                
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
            
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        
        return root