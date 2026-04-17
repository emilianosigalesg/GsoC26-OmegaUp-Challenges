#ENTRADA
line = input()
parts = line.split()
W = int(parts[0])
H = int(parts[1])

polyomino = []
for i in range(H):
    line = input()
    row = []
    for part in line.split():
        row.append(int(part))
    polyomino.append(row)

line = input()
parts = line.split()
F = int(parts[0])
G = int(parts[1])

board = []
for i in range(F):
    line = input()
    row = []
    for part in line.split():
        row.append(int(part))
    board.append(row)

#PROCESAMIENTO
#Polyomino
blocks = []
for r in range(H):
    for c in range(W):
        if polyomino[r][c] == 1:
            blocks.append((r, c))
if not blocks:
    print("YES")
    exit(0)

#Normalizar
def normalize(points):
    min_r = min(r for r, c in points)
    max_r = max(r for r, c in points)
    min_c = min(c for r, c in points)
    max_c = max(c for r, c in points)
    normalized = [(r - min_r, c - min_c) for (r, c) in points]
    height = max_r - min_r + 1
    width = max_c - min_c + 1
    return normalized, height, width

#Revisar
def fits(board, F, G, points, i, j):
    for dr, dc in points:
        board_row = i + dr
        board_column = j + dc
        if board_row >= F:
            return False
        if board_column >= G:
            return False
        if board[board_row][board_column] != 0:
            return False
    return True

#Rotar
def rotate90(points, h, w): 
    pointsr = []
    for r, c in points:
        rr = c
        cr = h - 1 - r
        pointsr.append((rr, cr))
    return pointsr, w, h

#Flip
def flip(points, h, w):
    pointsf = []
    for r, c in points:
        rf = r
        cf = w - 1 - c
        pointsf.append((rf, cf))
    return pointsf, h, w

#Revisar cada rotación y flip
for fliponce in range(2):
    if fliponce == 0:
        current = list(blocks)
        h, w = H, W
    else:
        current, h, w = flip(blocks, H, W)
        
    for rotation in range(4):
        points, height, width = normalize(current)
        for i in range(F - height + 1):
            for j in range(G - width + 1):
                if fits(board, F, G, points, i, j):
                    print("YES")
                    exit(0)
        if rotation < 3:
            current, h, w = rotate90(current, h, w)

print("IMPOSSIBLE")
exit(0)
