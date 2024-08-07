from collections import deque


def solve_puzzle(puzzle, source, destination):
    rows = len(puzzle)
    cols = len(puzzle[0])

    directions = [(0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U'), (1, 0, 'D')]

    queue = deque()
    queue.append(source)
    visited = set()
    visited.add(source)
    path = {source: (None, '')}

    while queue:
        x, y = queue.popleft()

        if (x, y) == destination:

            path_list = []
            directions_str = ''
            current = destination

            while current:

                path_list.append(current)
                direction = path[current][1]

                if direction:

                    directions_str += direction

                current = path[current][0]

            path_list.reverse()

            return path_list, directions_str

        for dx, dy, direction in directions:

            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and puzzle[nx][ny] == '-' and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))

                path[(nx, ny)] = ((x, y), direction)

    return None
