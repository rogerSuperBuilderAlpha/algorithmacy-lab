"""Is the BFS queue for Number of Islands bounded by O(min(m, n)) (key line 3389)? Build an H-tree island
in an N x N grid and measure the largest queue of a mark-on-enqueue BFS started where numIslands' scan
would start (the first land cell in row-major order). Also: sys.getsizeof(deque())."""
import sys
from collections import deque
print("sys.getsizeof(deque()) =", sys.getsizeof(deque()))
def htree(k):
    N = 2 ** k + 1
    g = [["0"] * N for _ in range(N)]
    def seg(r, c, half, horizontal, depth):
        if half < 1 or depth == 0:
            return
        if horizontal:
            for x in range(c - half, c + half + 1): g[r][x] = "1"
            ends = ((r, c - half), (r, c + half))
        else:
            for y in range(r - half, r + half + 1): g[y][c] = "1"
            ends = ((r - half, c), (r + half, c))
        nxt = half if horizontal else half // 2
        for er, ec in ends:
            seg(er, ec, nxt if horizontal else half // 2, not horizontal, depth - 1)
    seg(N // 2, N // 2, N // 4, True, 4 * k)
    return g
def bfs_peak(g):
    R, C = len(g), len(g[0])
    start = next((r, c) for r in range(R) for c in range(C) if g[r][c] == "1")
    seen = [[False] * C for _ in range(R)]; seen[start[0]][start[1]] = True
    q = deque([start]); peak = 1; size = 1
    while q:
        r, c = q.popleft()
        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == "1" and not seen[nr][nc]:
                seen[nr][nc] = True; q.append((nr, nc)); size += 1
        peak = max(peak, len(q))
    return peak, size
for k in range(5, 10):
    g = htree(k)
    peak, size = bfs_peak(g)
    print(f"H-tree in {len(g)}x{len(g)} grid: island cells {size}, peak BFS queue {peak}, min(m,n) = {len(g)}, ratio {peak/len(g):.2f}")
