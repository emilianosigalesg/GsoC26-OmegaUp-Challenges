# --- INPUT ---
W, H = map(int, input().split())

polyomino = []
for _ in range(H):
    row = list(map(int, input().split()))
    polyomino.append(row)

F, G = map(int, input().split())
board = []
for _ in range(F):
    row = list(map(int, input().split()))
    board.append(row)

# --- EXTRACT BLOCK COORDINATES ---
blocks = []
for r in range(H):
    for c in range(W):
        if polyomino[r][c] == 1:
            blocks.append((r, c))

if not blocks:
    print("YES")
    exit(0)

# --- GENERATE 8 ORIENTATIONS (4 rotations + 4 rotations of flipped) ---
def rotate90(points, h, w):
    """90° clockwise: (r, c) -> (c, h - 1 - r). New box size (w, h)."""
    return [(c, h - 1 - r) for r, c in points], w, h

def flip_horizontal(points, h, w):
    """Flip horizontally: (r, c) -> (r, w - 1 - c). Box size unchanged."""
    return [(r, w - 1 - c) for r, c in points], h, w

orientations = []
pts, h, w = blocks, H, W
for _ in range(4):
    orientations.append((list(pts), h, w))
    pts, h, w = rotate90(pts, h, w)

pts, h, w = flip_horizontal(blocks, H, W)
for _ in range(4):
    orientations.append((list(pts), h, w))
    pts, h, w = rotate90(pts, h, w)

# --- NORMALIZE EACH ORIENTATION TO ITS BOUNDING BOX ---
normalized_orientations = []
for points, h, w in orientations:
    min_r = min(r for r, c in points)
    max_r = max(r for r, c in points)
    min_c = min(c for r, c in points)
    max_c = max(c for r, c in points)
    normalized_points = [(r - min_r, c - min_c) for (r, c) in points]
    actual_h = max_r - min_r + 1
    actual_w = max_c - min_c + 1
    normalized_orientations.append((normalized_points, actual_h, actual_w))
orientations = normalized_orientations

# --- CHECK FIT AND PLACEMENT LOOP ---
def fits(board, F, G, points, i, j):
    """True if placing the shape at top-left (i, j) fits: all cells in bounds and 0."""
    for dr, dc in points:
        r, c = i + dr, j + dc
        if r < 0 or r >= F or c < 0 or c >= G or board[r][c] != 0:
            return False
    return True

for points, h, w in orientations:
    for i in range(F - h + 1):
        for j in range(G - w + 1):
            if fits(board, F, G, points, i, j):
                print("YES")
                exit(0)

# --- OUTPUT ---
print("IMPOSSIBLE")
