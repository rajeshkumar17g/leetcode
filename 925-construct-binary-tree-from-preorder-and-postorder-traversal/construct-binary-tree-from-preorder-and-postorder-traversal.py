class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
        def maketree():
            node=TreeNode(postorder.pop())
            if node.val!=preorder[-1]:
                node.right=maketree()
            if node.val!=preorder[-1]:
                node.left=maketree()
            preorder.pop()
            return node
        #----------------------
        return maketree()
