import os
import sys

from common.common import get_input

sys.setrecursionlimit(99999)
cwd = os.getcwd()
c = get_input(cwd)


def valid_pipe_coords(pipe, coord):
    i, j = coord
    dirs = {
        'n': (i - 1, j),
        'w': (i, j - 1),
        'e': (i, j + 1),
        's': (i + 1, j)
    }
    pipes = {
        '|': ('n', 's'),
        '-': ('e', 'w'),
        'L': ('n', 'e'),
        'J': ('n', 'w'),
        'F': ('s', 'e'),
        '7': ('w', 's')
    }
    return list(dirs[d] for d in pipes[pipe])


def is_valid_direction_from_coord(current_coord, next_coord):
    i, j = next_coord
    k, l = current_coord
    next_pipe = c[i][j]
    if next_pipe == '.':
        return False
    current_pipe = c[k][l]

    valid_from_current = False
    if current_pipe != 'S':
        if next_coord in valid_pipe_coords(current_pipe, current_coord):
            valid_from_current = True
    else:
        valid_from_current = True

    if next_pipe == 'S' and valid_from_current:
        return True

    return valid_from_current and current_coord in valid_pipe_coords(pipe=next_pipe, coord=next_coord)


def find_start():
    i = -1
    j = -1
    for k, line in enumerate(c):
        if 'S' in line:
            i = k
            j = line.index('S')
            break
    return i, j


start = find_start()


def find_loop(coords, visited):
    visited.append(coords)
    i, j = coords

    # n w e s
    for next_coord in (
            (i - 1, j),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j),
    ):
        try:
            k, l = next_coord
            if c[k][l] == 'S' and len(visited) > 2 and is_valid_direction_from_coord(coords, next_coord):
                return visited
            if next_coord not in visited and is_valid_direction_from_coord(coords, next_coord):
                return find_loop(next_coord, visited)
        except IndexError:
            continue

    # dead end
    return visited[:-1]


loop_nodes = find_loop(start, [])

vert_left = ('7', '|', 'J')
vert_right = ('F', '|', 'L')


def bfs(map, visited, coord, vert=True, hor=True):
    i, j = coord
    visited.add(coord)
    queue = []

    curr = map[i][j]

    # generate next coords
    v_coords = [(i - 1, j), (i + 1, j)]
    h_coords = [(i, j-1), (i, j+1)]
    next_coords = []
    if vert:
        next_coords.extend(v_coords)
    if hor:
        next_coords.extend(h_coords)

    for next_coord in next_coords:
        k, l = next_coord
        if k < 0 or l < 0:
            continue
        try:
            nex = map[k][l]
            if next_coord in visited:
                continue
            if next_coord in loop_nodes and abs(k-i) == 1:
                if nex in vert_left and map[k][l+1] in vert_right:
                        queue.append(tuple((next_coord, True, False)))

            if next_coord not in loop_nodes:
                queue.append(tuple((next_coord, True, True)))

        except IndexError:
            continue

    for (n, vert, hor) in queue:
        visited = bfs(map, visited, n, vert, hor)

    return visited


visited = bfs(c, set(), ((0,0)), True, True)

all_possible = set()
for i in range(len(c)):
    for j in range(len(c[0])):
        all_possible.add((i, j))

visited = set(visited).difference(loop_nodes)
inside_loop = len(all_possible) - len(visited) - len(loop_nodes)
print(inside_loop)
