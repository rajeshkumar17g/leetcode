class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3]
        def maketree():
            if postorder!=[]:
                node=TreeNode(postorder.pop()) # node=[1]
                if node.val!=preorder[-1]:
                    node.right=maketree()
                if node.val!=preorder[-1]:
                    node.left=maketree()
                preorder.pop()
                return node

        return maketree()