# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
import math
from typing import Optional


       

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
       # Initialize result
       self.maxSumOfAllPaths = float("-inf")
       if root is None:
         return 0;
       # Compute and return result
       self.findMaxUtil(self,root)
       return self.maxSumOfAllPaths
    
    def findMaxUtil(self,root):
        res=0
        # Base Case
        if root is None: 
          return
        # l and r store maximum path sum going through left
        # # and right child of root respectively  
        leftSum= max(self.findMaxUtil(self,root.left),0)
        rightSum= max(self.findMaxUtil(self,root.right),0)
        # Max path for parent call of root. This path
        # must include at most one child of root
        max_single = max(max(leftSum, rightSum) + root.data, root.data)
        # Max top represents the sum when the node under
        # # consideration is the root of the maxSum path and
        # # no ancestor of root are there in max sum path
        max_top = max(max_single, leftSum+rightSum + root.data)
        # Static variable to store the changes
        # # Store the maximum result
        return max_top       
# Driver code
if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(-25)
    root.right.right.left = TreeNode(3)
    root.right.right.right = TreeNode(4)
    
    s=Solution()
    print ("Max path sum is: "+ Solution.maxPathSum(Solution,root))