from heapq import heappush, heappop


def input():
    with open("2023/dag_17/input.txt", 'r') as file:
        content = [[int(i) for i in line.strip()] for line in file]
        
    return content


def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()


def find_path(grid):
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return hl
        
        if (r, c, dr, dc, n) in seen:
            continue
        
        seen.add((r, c, dr, dc, n))
        
        if n < 3 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))
                
        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))


def main():    
    grid = input()
    optimal_hl = find_path(grid)
    print(optimal_hl)
    
    
if __name__ == "__main__":
    main()
    