class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if p == q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


sol = Solution()
a = TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))
b = TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))
print(sol.isSameTree(a, b))
