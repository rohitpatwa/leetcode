# Construct a tree with all functions mentioned. Do a pre-order traversal of the tree and only add alive people to the order.

class Person:
    def __init__(self, childName):
        self.name = childName
        self.children = []
        self.alive = True
        

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Person(kingName)
        self.name2node = {kingName:self.king}

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.name2node[parentName]
        child = Person(childName)
        self.name2node[childName] = child
        parent.children.append(child)
        

    def death(self, name: str) -> None:
        person = self.name2node[name]
        person.alive = False

    def getInheritanceOrder(self) -> List[str]:
        order = []
        self.preOrder(self.king, order)
        return order
        
        
    def preOrder(self, node, order):
        if not node:
            return
        
        if node.alive:
            order.append(node.name)
        for c in node.children:
            self.preOrder(c, order)
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()