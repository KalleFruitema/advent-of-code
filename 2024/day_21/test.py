@cache
def move(x, y, gx, gy, keypad):
    grid = numpad if keypad == "num" else dirpad
    pq = [(0, "", x, y)]
    seen = set()
    
    while pq:
        steps, moves, x, y = heappop(pq)
        
        if (x, y) == (gx, gy):
            return moves
        
        if (x, y) in seen:
            continue
        seen.add((x, y))
        
        for dx, dy, char in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "#":
                heappush(pq, (steps + 1, moves + char, nx, ny))
                
                
                
                
                
    # elif gx == x:
    #     char = "v" if gy > y else "^"
    #     return char * abs(gy - y)
    # elif gy == y:
    #     char = ">" if gx > x else "<"
    #     return char * abs(gx - x)
    
    # if gx > x:
    #     moves = ">" * abs(gx - x)
    #     char = "v" if gy > y else "^"
    #     return moves + char * abs(gy - y)
    # else:
    #     char = "v" if gy > y else "^"
    #     moves = char * abs(gy - y)
    #     return moves + "<" * abs(gx - x)