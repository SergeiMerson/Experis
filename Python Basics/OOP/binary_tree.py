class Tree:

    def __init__(self):
        self.tree = [None, None, None]

    def add(self, x, node: list = None):
        if node is None:
            node = self.tree
        l, c, r = node[0], node[1], node[2]
        if c is None:
            node[1] = x
        elif x < c:
            if l is None:
                node[0] = [None, x, None]
            else:
                self.add(x, node[0])
        elif x > c:
            if r is None:
                node[2] = [None, x, None]
            else:
                self.add(x, node[2])

    def traverse_with_strategy(self, node=None, strategy=print):
        if node is None:
            node = self.tree

        if node[0] is not None:
            self.traverse_with_strategy(node[0], strategy)

        strategy(node[1])

        if node[2] is not None:
            self.traverse_with_strategy(node[2], strategy)


class Strategy:
    def __init__(self, sep=', ', end='\n'):
        self.storage = []
        self.sep = sep
        self.end = end

    def print_storage(self):
        print(sum(self.storage), ':', end=' ')
        print(*self.storage, sep=self.sep, end=self.end)

    def accumulate(self, x):
        self.storage.append(x)
        self.print_storage()


tree = Tree()
[tree.add(i) for i in [10, 9, 8, 7, 12, 15, 52, 31, 1, 14, 29, 19, 13]]
tree.traverse_with_strategy(strategy=Strategy(sep=' - ').accumulate)
