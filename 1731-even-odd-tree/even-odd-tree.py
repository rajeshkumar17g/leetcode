# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return []
        
       
        q=deque([root])
        l=0
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            if l%2==0:
                for index in range(len(level)):
                    if level[index]%2==0:
                        return False
                    if index+1<len(level) and level[index]>=level[index+1]:
                        return False
            else:
                for index in range(len(level)):
                    if level[index]%2==1:
                        return False
                    if index+1<len(level) and level[index]<=level[index+1]:
                        return False
            l=l+1 
        return True

