from queue import Queue


def outOfBounds(N, row, column):
    return row < 0 or row >= N or column < 0 or column >= N


def valid_pos(grid, N, visiteds, row, column):
    # Check if the coordenate is out of the bounds
    if outOfBounds(N, row, column):
        return False
    # Check if we already visited this coordenate
    for r, c, _ in visiteds:
        if (row, column) == (r, c):
            return False
    # Check if there is a Wall
    if grid[row][column] == 'X':
        return False
    # Check if there is an infected near us
    s = [(row + 1, column), (row - 1, column),
         (row, column - 1), (row, column + 1)]
    for r, c in s:
        if not outOfBounds(N, r, c):
            if grid[r][c] == 'Y':
                return False
    return True


def BFS(grid, N, row, column):
    '''An implementation of Breath first search 
    algorithm for this Grid
    '''
    queue = Queue()
    visiteds = []
    queue.put((row, column, 0))
    while not queue.empty():
        node = queue.get()
        r, c, steps = node
        if valid_pos(grid, N, visiteds, r, c):
            s = grid[r][c]
            if s == 'C':
                return steps
            queue.put((r + 1, c, steps + 1))
            queue.put((r - 1, c, steps + 1))
            queue.put((r, c - 1, steps + 1))
            queue.put((r, c + 1, steps + 1))
            visiteds.append(node)
    return -1


def MBFS(grid, N, row, column):
    '''A modification of the last BFS 
    to check the new incorporations to the grid
    '''
    queue = Queue()
    visiteds = []
    queue.put((row, column, 0))
    while not queue.empty():
        node = queue.get()
        r, c, steps = node
        if valid_pos(grid, N, visiteds, r, c):
            s = grid[r][c]
            if s == 'H':
                return steps
            elif s == 'U':
                queue.put((r - 3, c, steps + 1))
            elif s == 'L':
                queue.put((r, c - 3, steps + 1))
            elif s == 'R':
                queue.put((r, c + 3, steps + 1))
            elif s == 'D':
                queue.put((r + 3, c, steps + 1))
            queue.put((r + 1, c, steps + 1))
            queue.put((r - 1, c, steps + 1))
            queue.put((r, c - 1, steps + 1))
            queue.put((r, c + 1, steps + 1))
            visiteds.append(node)
    return -1


def phase1():
    file = open("../maps/map.txt", "r")
    info = file.read().strip().split('\n')
    N = int(info[0])
    grid = list(map(lambda s: list(s), info[1:-1]))
    (row, column) = tuple(map(lambda x: int(x), info[-1].split()))
    steps = BFS(grid, N, row, column)
    print("Phase 1:", steps)


def phase2():
    file = open("../maps/map2.txt", "r")
    info = file.read().strip().split('\n')
    N = int(info[0])
    grid = list(map(lambda s: list(s), info[1:-1]))
    (row, column) = tuple(map(lambda x: int(x), info[-1].split()))
    steps = MBFS(grid, N, row, column)
    print("Phase 2:", steps)


phase1()
phase2()
