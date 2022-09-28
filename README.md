## Remove Invalid Parenthesis

The time complexity of the above code is O(2^N)
The main idea to solve this problem is to use Backtracking.
The recursion tree is where we have skipped the 3rd and 6th characters.

## Maximum Absolute Difference in BST

My solution would be to traverse the tree, and for every node, find the maximum value node in its left and right subtree. If the difference between the node and its descendants is more than the maximum difference found so far, update it. The time complexity of this solution is O(n^2), where n is the total number of nodes in the binary tree.

## Maximum Path Sum in a Binary Tree

If the root is NULL, return 0(Base Case)
Call the recursive function to find the max sum for the left and the right subtree
In a variable store the maximum of (root->data, maximum of (leftSum, rightSum) + root->data)
In another variable store the maximum of previous step and root->data + leftSum + rightSum
Return the maximum of the previous step
The time complexity of the above code is O(N)

## Lexicographical Numbers

Time Complexity: O(N)
Using DFS: Always multiply temp by 10 till temp \* 10 is greater than n
Increment temp by 1 when the last digit of temp is not equal to 9
