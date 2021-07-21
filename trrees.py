class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' '*self.get_level()*3
        print(f"{spaces}__|{self.data}")
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode('Electronic')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('mac'))
    laptop.add_child(TreeNode('MS surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    cellphone = TreeNode('cellphone')
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("GooglePixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode('tv')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('Lg'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()