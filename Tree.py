class Coordinate:
    def __init__(self, x = 0, y = 0):
        self.brs = x
        self.kol = y
    
    def getBrs():
        return self.brs
    
    def getKol():
        return self.kol

class Tree:
    def __init__(self, data=None):
        self.key = data
        self.children = []
 
    def set_root(self, data):
        self.key = data
 
    def add(self, node):
        self.children.append(node)
 
    def search(self, key):
        if self.key == key:
            return self
        for child in self.children:
            temp = child.search(key)
            if temp is not None:
                return temp
        return None

    def getRoot():
        return self.key

TreeList = []

input

def BFS(matriks, startBrs, startKol, goalBrs, goalKol):
    finish = False
    start = Coordinate(startBrs, startKol)
    tree = Tree(start)
    TreeList.append(tree)
    queue = [start]
    while (!finish):
        
