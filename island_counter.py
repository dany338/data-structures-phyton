def get_edges(i, j, matrix):
    edges = []
    if i < len(matrix) - 1:
        edges.append( (i+1, j) ) 
    if j < len(matrix[0]) - 1:
        edges.append( (i, j+1) ) 
    return edges

def bfs(matrix, visited, x, y, result):
    queue = [(x, y)]
    count = 0
    while len(queue) > 0:
        i, j = queue.pop(0)
        if matrix[i][j] == 0:
            continue
        if (i, j) in visited:
            continue
        count += 1
        visited[(i, j)] = True
        edges = get_edges(i, j, matrix)
        for (u, v) in edges:
            if (u, v) not in visited:
                queue.append( (u, v) )
    if count > 0:
        result.append(count)

# A: full ones matrix 
# runtime complexity: O(n*m) + O((n-1) * (m-1))* O(1)
#   cost:  O(nxm)
# space complexity: O(nxm)

def island_counter(matrix):
    result = []
    visited = {} 
    for i in range(len(matrix)): # O(n)
        for j in range(len(matrix[0])): # O(m)
            if matrix[i][j] == 1 and (i, j) not in visited:
                bfs(matrix, visited, i, j, result)  # bfs = O(|V| + |E|) -> O(nxm), ... O(1)
    return result

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

print(island_counter(matrix)) # [2, 2, 5, 1, 2]