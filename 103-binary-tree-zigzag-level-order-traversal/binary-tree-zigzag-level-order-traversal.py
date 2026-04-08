# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        #FIFO
        q=deque([root]) # q=[root]. # deque array. .append(). .popleft()
        res=[]
        l=1
        while q: # while q is not empty 
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            if l%2==1:
                 res.append(level)
            else:
                res.append(level[::-1])
            l=l+1
        
        return res