# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        sol = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                sol.append(current.val)
                current = current.left

            current = stack.pop()
            current = current.right
        return sol
            
def main():
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    sol = Solution()
    print(sol.inorderTraversal(root))

if __name__ == "__main__":
    main()