# Time Complexity = O(n) | Space Complexity O(n/2) = O(n)

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFSSolution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        if root is None: return result
        queue = deque()
        node = queue.append(root)
        while len(queue) != 0:
            size = len(queue)
            curr_arr = []
            for i in range(size):
                node = queue.popleft()
                curr_arr.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(curr_arr)

        return result

# Time Complexity = O(n) | Space Complexity O(h) (only recursive stack space)
class DFSSolution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        self.result = []
        self.dfsHelper(root, 0)
        return self.result

    def dfsHelper(self, node: TreeNode, level: int):
        # base case
        if node is None: return

        size = len(self.result)
        if size == level:
            self.result.append([])
        self.result[level].append(node.val)

        self.dfsHelper(node.left, level + 1)
        self.dfsHelper(node.right, level + 1)

