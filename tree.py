import pprint

def dfs_rec(ptr):
    # pre-order(T) = [  T.data  + pre-order(T.left) + pre-order(T.right) ]
    print(ptr.name)
    for c in ptr.children:
        dfs_rec(c)

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        new_node = Node(name)
        self.children.append(new_node)
        return new_node

    def dfs(self):
        dfs_rec(self)

    def dfs_iter(self):
        stack = [self]
        while len(stack) > 0:
            curr = stack.pop()
            print(curr.name)
            for index in reversed(range(0, len(curr.children))):
                stack.append(curr.children[index])

# runtime complexity (b^n_levels), O(|V| + |E|)
# space complexity O(|V|), O(N)
def bfs(ptr):
    queue = [ (ptr, 0)]        
    dicc = {}
    while len(queue) > 0:
        curr, level = queue.pop(0)
        if level not in dicc:
            dicc[level] = []    
        dicc[level].append(curr.name)
        for c in curr.children:
            queue.append( (c, level + 1) )
    pprint.pprint(dicc)

root = Node("A")
b = root.addChild("B")
c = root.addChild("C")
d = root.addChild("D")

e = b.addChild("E")
f = b.addChild("F")

f.addChild("I")
f.addChild("J")

root.dfs() # 
print()
root.dfs_iter() # 
print()
bfs(root)