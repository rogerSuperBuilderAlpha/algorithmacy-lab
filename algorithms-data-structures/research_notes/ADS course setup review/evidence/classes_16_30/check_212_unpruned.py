"""#212 without the dead-branch pruning (`if not node: parent.pop(ch)`): same results as the board solution?"""
import copy, random, time
import board_solutions as S
random.seed(5)
def findWords_unpruned(board, words):
    root = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = word
    rows, cols, found = len(board), len(board[0]), []
    def dfs(r, c, parent):
        ch = board[r][c]; node = parent[ch]
        if '$' in node:
            found.append(node.pop('$'))
        board[r][c] = '#'
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in node:
                dfs(nr, nc, node)
        board[r][c] = ch
    for r in range(rows):
        for c in range(cols):
            if board[r][c] in root:
                dfs(r, c, root)
    return found
same = 0
for t in range(2000):
    R, C = random.randint(1, 4), random.randint(1, 4)
    b = [[random.choice("abc") for _ in range(C)] for _ in range(R)]
    ws = list({"".join(random.choice("abc") for _ in range(random.randint(1, 6))) for _ in range(random.randint(1, 15))})
    same += sorted(S.findWords(copy.deepcopy(b), ws)) == sorted(findWords_unpruned(copy.deepcopy(b), ws))
print("identical results on", same, "of 2000 random cases")
board = [["a"] * 12 for _ in range(12)]
words = ["a" * k for k in range(1, 11)] + ["a" * 9 + "b"]
for f in (S.findWords, findWords_unpruned):
    t0 = time.perf_counter(); out = f(copy.deepcopy(board), words)
    print(f"{f.__name__}: {len(out)} words, {time.perf_counter()-t0:.2f} s on 12x12 all-'a' board")
