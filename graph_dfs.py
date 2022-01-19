import pprint


class DFS: 
    def __init__(self):
        self.visited = {}

    def dfs_rec(self, graph, current, target, path):
        self.visited[current] = True
        if current == target:
            print("path dfs", path)
            return
        for next_node in graph[current]:
            if next_node not in self.visited:
                self.dfs_rec(graph, next_node, target, path + [next_node])

def dfs(graph, source, target):
    stack = [(source, [source])]
    visited = {}
    while len(stack) > 0:
        current, path = stack.pop()
        if current == target:
            print("path!", path)
            break
        visited[current] = True
        for n in graph[current]:
            if n not in visited:
                stack.append( (n, path + [n]) )
     
# runtime complexity: O(|V| + |E|)
# space complexity: O(|V|)
def bfs(graph, source, target):
    queue = [(source, [source])]
    visited = {}
    while len(queue) > 0:
        current, path = queue.pop(0)
        if current == target:
            print("path!", path)
            break
        visited[current] = True
        for n in graph[current]:
            if n not in visited:
                queue.append( (n, path + [n]) )


airports = ["A", "B", "C", "D", "F", "G"]
n = len(airports)
routes = [  
    ["A", "B"],
    ["B", "C"],
    ["C", "D"],
    ["A", "C"],
    ["A", "D"],
    ["C", "A"],
    ["B", "F"]
]

graph = {}
for v in airports:
    graph[v] = [] 

for (u, v) in routes:
    graph[u].append(v)

pprint.pprint(graph)

bfs(graph, source = 'A', target = 'F')
dfs(graph, source = 'A', target = 'F')

alg = DFS()
alg.dfs_rec(graph, 'A', target = 'G', path = ['A'])