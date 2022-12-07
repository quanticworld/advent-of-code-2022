from anytree import NodeMixin


class NodeInfo:  # Just an example of a base class
    def __init__(self, name, depth, size, sum_children):
        self.name = name
        self.size = size
        self.sum_children = 0


class FileNode(NodeInfo, NodeMixin):  # Add Node feature
    def __init__(self, name, size, sum_children, parent=None, children=None):
        super(NodeInfo, self).__init__()
        self.name = name
        self.size = size
        self.sum_children = sum_children
        self.parent = parent
        if children:
            self.children = children


