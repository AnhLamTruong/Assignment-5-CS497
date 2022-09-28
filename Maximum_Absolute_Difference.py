import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMaximumDifference(self, root: TreeNode) -> int:
        if not root:return 0
        arr=[]
        def helper(node):
            if node:
                arr.append(node.val)
                helper(node.left)
                helper(node.right)
        helper(root)
        arr.sort()
        ans=sys.maxsize
        for i in range(len(arr)-1):
            ans=max(ans,abs(arr[i]-arr[i+1]))
        return ans

root = TreeNode()
root.val=TreeNode(4)
root.left.val = TreeNode(2)
root.right.val = TreeNode(6)
root.left.left.val = TreeNode(1)
root.left.right.val = TreeNode(3)

print (getMaximumDifference(root))
