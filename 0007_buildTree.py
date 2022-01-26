# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

# 二叉树前序遍历的顺序为：

    # 先遍历根节点；

    # 随后递归地遍历左子树；

    # 最后递归地遍历右子树。

# 二叉树中序遍历的顺序为：

    # 先递归地遍历左子树；

    # 随后遍历根节点；

    # 最后递归地遍历右子树。



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            
            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(self, preorder_l, preorder_r, inorder_l, inorder_r):
            root_pre_idx = preorder_l
            root_in_idx = inorder.index(preorder[root_pre_idx])

            root = TreeNode(preorder[root_pre_idx])
            size_left_subtree = root_in_idx - inorder_l

            root.left = myBuildTree(preorder_l+1, preorder_l + size_left_subtree, inorder_l, root_in_idx-1)
            root.right = myBuildTree(preorder_l + size_left_subtree + 1, preorder_r, root_in_idx + 1, inorder_r)
            return root
        n = len(preorder)
        return myBuildTree(0, n-1, 0, n-1)

