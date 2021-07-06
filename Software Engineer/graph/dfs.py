class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        if self.name not in array:
			array.append(self.name)
			for child in self.children:
				child.depthFirstSearch(array)
		
		return array
