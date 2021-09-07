# -- coding: utf-8 --
# @Time    : 2021/9/7 0007 13:42
# @Author  : TangKai
# @Team    : SuperModel
# @File    : BiSortTree.py


# 定义二叉树的结点
class BiSortTreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 定义一颗二叉排序树
class BiSortTree(object):

    # 根结点
    def __init__(self, root=None):
        self.root = root

    # 插入结点方法a, 采用递归的方法
    def insert_a(self, value):
        if self.root is None:
            self.root = BiSortTreeNode(value)
        else:
            self.insert_node(value=value, tree_node=self.root)

    # 插入结点的子函数
    def insert_node(self, value=None, tree_node=None):

        if tree_node.value > value:
            if tree_node.left is None:
                tree_node.left = BiSortTreeNode(value)
            else:
                self.insert_node(value, tree_node.left)
        else:
            if tree_node.right is None:
                tree_node.right = BiSortTreeNode(value)
            else:
                self.insert_node(value, tree_node.right)

    # 插入结点方法b, 采用循环的方式
    def insert_b(self, value):
        if self.root is None:
            self.root = BiSortTreeNode(value)
        else:
            _root = self.root
            while True:
                if value > _root.value:
                    if _root.right is None:
                        _root.right = BiSortTreeNode(value)
                        return
                    else:
                        _root = _root.right
                else:
                    if _root.left is None:
                        _root.left = BiSortTreeNode(value)
                        return
                    else:
                        _root = _root.left

    # 前序遍历
    def pre_order_tree(self):
        self.pre_order(self.root)

    def pre_order(self, root):
        if root is None:
            return

        self.pre_order(root.left)

        self.pre_order(root.right)
        print(root.value)


if __name__ == '__main__':
    bt = BiSortTree()
    bt.insert_a(12)
    bt.insert_a(1)
    bt.insert_a(111)
    bt.insert_a(1122)
    # bt.insert_node_b(12)
    # bt.insert_node_b(1)
    # bt.insert_node_b(111)
    # bt.insert_node_b(1122)

    bt.pre_order_tree()
