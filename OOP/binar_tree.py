class Tree:
    def __init__(self,val):
        self.root=val
        self.left=None
        self.right=None

tr1=Tree(8)
tr2=Tree(3)
tr3=Tree(6)
tr4=Tree(1)


tr1.left=tr2
tr2.right=tr3
tr2.left=tr4
# print(tr1.root)             # 8 tr1.root
# print(tr1.left.root)        # 3 tr2.root
# print(tr2.right.root)       # 6 tr3.root
# print(tr1.left.right.root)  # 6 tr3.root
# print(tr1.left.left.root)   # 1 tr4.root





class Tree2:
    def __init__(self,val):
        self.root=val
        self.right=None
        self.left=None

    def insert(self,data):
        if data>=self.root:
            if self.right is None:
                self.right=Tree2(data)
            else:
                self.right.insert(data)
        else:
            if self.left is None:
                self.left=Tree2(data)
            else:
                self.left.insert(data)

    def __repr__(self):
        lines, *_ = self.__display()
        for line in lines:
            print(line)
        return '\n'

    def __display(self):
        line = f"{self.root}"
        width = len(line)

        # todo none child
        if self.right is None and self.left is None:
            return [line], width, 1, width // 2

        # todo right child
        if self.left is None:
            lines, n, p, x = self.right.__display()
            return [line + x * '_' + (n - x) * ' ', (width + x) * ' ' + '\\' + (n - x - 1) * ' '] + \
                   [width * ' ' + line for line in lines], n + width, p + 2, width // 2

        # todo left child
        if self.right is None:
            lines, n, p, x = self.left.__display()
            return [(x + 1) * ' ' + (n - x - 1) * '_' + line, x * ' ' + '/' + (n - x - 1 + width) * ' '] + \
                   [line + width * ' ' for line in lines], n + width, p + 2, n + width // 2

        # todo both child
        if self.right is not None and self.left is not None:
            left, n, p, x = self.left.__display()
            right, m, q, y = self.right.__display()
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            return [
                       (x + 1) * ' ' + (n - x - 1) * '_' + line + y * '_' + (m - y) * ' ',
                       x * ' ' + '/' + (n - x - 1 + width + y) * ' ' + '\\' + (m - y - 1) * ' '
                   ] + [a + width * ' ' + b for a, b in zip(left, right)], n + m + width, max(p,
                                                                                              q) + 2, n + width // 2











tree1=Tree2(8)
tree1.insert(3)
tree1.insert(10)
tree1.insert(1)
tree1.insert(6)
tree1.insert(11)
tree1.insert(4)
tree1.insert(7)
tree1.insert(11)
tree1.insert(5)


print(tree1)