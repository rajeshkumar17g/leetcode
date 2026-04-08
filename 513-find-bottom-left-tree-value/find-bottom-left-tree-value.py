# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return []
        #FIFO
        q=deque([root]) # q=[root]. # deque array. .append(). .popleft()
        res=[]

        while q: # while q is not empty 
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            res.append(level)
        
        return res[-1][0]