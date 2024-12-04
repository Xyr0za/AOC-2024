cont = [list(i.strip()) for i in open("day4input.txt").readlines()]

def get_neighbors(matrix, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    neighbors = []

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0,0), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append(matrix[nx][ny])
    
    return neighbors

def check(matrix):
    ret = 0
    m = matrix.copy()
    mas = ["MAS", "SAM"]
    d = ''.join([m[0][0], m[1][1], m[2][2]])
    a = ''.join([m[0][2], m[1][1], m[2][0]])
    ret += 1 if (d in mas and a in mas) else 0
    return ret

t = 0

for x in range(len(cont)):
    for y in range(len(cont[x])):
        if x in [0, 139] or y in [0, 139]:
            continue
        if cont[x][y] == "A":
            neighbours = get_neighbors(cont, x,y)
            matrix = [neighbours[:3], neighbours[3:6], neighbours[6:]]

            t += check(matrix) 

print(t)
