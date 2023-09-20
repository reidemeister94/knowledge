class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def dfs(self, array):
        if self.name not in array:
            array.append(self.name)
            for child in self.children:
                child.dfs(array)

        return array
