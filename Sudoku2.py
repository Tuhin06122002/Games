def showgrid():
    global grid

    for y in range(9):
        for x in range(9):
            print(grid[y][x],end=" ")
        print()
    print()

def isPossible(x,y,n):
    global grid

    for i in range(9):
        if grid[y][i]==n:
            return 0
        if grid[i][x]==n:
            return 0

    xf = (x//3)*3
    yf = (y//3)*3

    for i in range(3):
        for j in range(3):
            if grid[yf+i][xf+j]==n:
                return 0
    
    return 1

def solve():
    global grid

    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if isPossible(x,y,n):
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return
    showgrid()

grid=[[3,0,6,5,0,8,4,0,0],
      [5,2,0,0,0,0,0,0,0],
      [0,8,7,0,0,0,0,3,1],
      [0,0,3,0,1,0,0,8,0],
      [9,0,0,8,6,3,0,0,5],
      [0,5,0,0,9,0,6,0,0],
      [1,3,0,0,0,0,2,5,0],
      [0,0,0,0,0,0,0,7,4],
      [0,0,5,2,0,6,3,0,0]]
showgrid()
input()
solve()