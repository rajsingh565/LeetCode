# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs ?
        # need to get back the node and depth of each node
        # we can then compare whose depth is greater
        # greater depth means its the lowest leaf
        # if node is same, i.e left depth is same as right depth, we return node as its the answer

        def dfs(node, depth):
            if not node:
                return (None, depth+1)  # counting current node's height as +1
            
            l, ld = dfs(node.left, depth+1)
            r, rd = dfs(node.right, depth+1)
            #if left has more depth, we'd like to explore there
            # if l > r, no way we will get common ancestor in r as it has lesser nodes
            # we return left node and depth +1 accounting that the current node has been accounted in depth
            if ld > rd:
                return l, ld
            #if right has more depth, we'd like to explore there
            # if l < r, no way we will get common ancestor in l as it has lesser nodes to explore
            # we return right node and depth +1 accounting that the current node has been accounted in depth
            elif rd > ld:
                return r, rd
            # base case l == r
            # can return node and anyone from left and right depth
            return (node, rd)
        node, _ = dfs(root, 0)
        return node