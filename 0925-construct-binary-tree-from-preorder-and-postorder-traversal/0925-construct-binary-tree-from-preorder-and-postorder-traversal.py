# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        pre_i = 1
        post_i = 0
        N = len(preorder)
        root = TreeNode(preorder[0])
        stack = [root]

        while pre_i < N:

            newNode = TreeNode(preorder[pre_i])

            # Condition to check if should append as right child
            while stack[-1].val == postorder[post_i]:
                post_i += 1
                stack.pop()

                # Append right
                if stack[-1].val != postorder[post_i]:
                    stack[-1].right = newNode
                    break
            else:
                # Append Left
                stack[-1].left = newNode

            stack.append(newNode)
            pre_i += 1


        return root 