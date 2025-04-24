# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        node = root

        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                else:
                    node = stack.pop()
                    ans.append(node.val)
                    node = node.right
        return ans
        