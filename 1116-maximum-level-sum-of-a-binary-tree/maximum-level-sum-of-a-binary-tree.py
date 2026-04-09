class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return []
        
        res=[]
        q=deque([root])

        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            res.append(sum(level))
        max_level=0
        max_sum=res[0]
        for index in range(len(res)):
            if res[index]>max_sum:
                max_sum=res[index]
                max_level=index

        return max_level+1