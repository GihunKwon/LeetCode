# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        answer = None
        cur_node = root
        while cur_node:
            if cur_node.val == val:
                answer = cur_node
                break
            elif cur_node.val < val:
                cur_node = cur_node.right
            elif cur_node.val > val:
                cur_node = cur_node.left
        return answer

        