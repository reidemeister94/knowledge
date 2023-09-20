class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def bfs(self, array):
        queue = []
        array.append(self.name)
        queue.append(self)

        while queue:
            elem = queue.pop(0)
            for child in elem.children:
                if child not in array:
                    queue.append(child)
                    array.append(child.name)
        return array
