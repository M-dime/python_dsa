class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


class Recursive_traversal:
    # recursive
    def RPreoder_traversal(self, root, s):
        if root == None:
            return s
        s += (str(root.val) + "-")
        s = str(self.RPreoder_traversal(root.left, s))
        s = str(self.RPreoder_traversal(root.right, s))
        return s

    def RPostoder_traversal(self, root, s):
        if root == None:
            return s
        s = str(self.RPostoder_traversal(root.left, s))
        s = str(self.RPostoder_traversal(root.right, s))
        s += (str(root.val) + "-")
        return s

    def RInorder_traversal(self, root, s):
        if root == None:
            return s
        s = str(self.RInorder_traversal(root.left, s))
        s += (str(root.val) + "-")
        s = str(self.RInorder_traversal(root.right, s))
        return s
class Iterative:
    def ipreorder(self,root,s):
        stack = []
        curr = root
        while True:
            if curr is not None :
                stack.append(curr)
                curr= curr.left

            if len(stack)==0:
                break

            curr = stack.pop()
            s += (curr.data + " ")
            curr = curr.right
        return s


class BinaryTree(Recursive_traversal,Iterative):
    def __init__(self, root):
        self.root = TreeNode(root)

# iterative


if __name__ == '__main__':
    #      2
    #    /  \
    #   3    4
    #  / \  / \
    # 5  6 7   8
    tree = BinaryTree(2)
    tree.root.left = TreeNode(3)
    tree.root.left.left = TreeNode(5)
    tree.root.left.right = TreeNode(6)
    tree.root.right = TreeNode(4)
    tree.root.right.left = TreeNode(7)
    tree.root.right.right = TreeNode(8)
    print(tree.RPreoder_traversal(tree.root,""))
    print(tree.RPostoder_traversal(tree.root,""))
    print(tree.RInorder_traversal(tree.root,""))
    print(tree.ipreorder(tree.root,""))