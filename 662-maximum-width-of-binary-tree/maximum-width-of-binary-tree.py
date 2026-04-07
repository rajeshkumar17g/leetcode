class Solution:
    """My iterative BFS Solution"""
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:     
        if not root:
            return 0
        queue = deque([(root, 0)])
        res = 0

        while queue:
            level = len(queue)
            curr = []
            for _ in range(level):
                node, index = queue.popleft()
                curr.append(index)
                if node.left:
                    queue.append((node.left, index*2))
                if node.right:
                    queue.append((node.right, index*2+1))
            curr_size = curr[-1] - curr[0] + 1
            res = max(res, curr_size)
        return res