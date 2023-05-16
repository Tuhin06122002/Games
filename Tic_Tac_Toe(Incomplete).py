def fill_up(n,mat,ct):
    if n>10 or n<0:
        #alert()
        print("Invalid Move")
    if ct%2==0:
        a=10
    else:
        a=1
    
    if mat[(n-0.5)//3][(n+2)%3] == 0:
        mat[(n-0.5)//3][(n+2)%3] = a
        ct += 1
    else:
        #alert()
        print("That space is already filled up.")


def check_win(a,arr):   #a = ct+1
    if a%2==0:
        b=10
    else:
        b=1

    for i in range(3):
        if sum(arr[i][0],arr[i][1],arr[i][2]) == 3*b or sum(arr[0][i],arr[1][i],arr[2][i]) == 3*b:
            #code for a wins
            return 1
    
    if sum(arr[0][0],arr[1][1],arr[2][2])==3*b or sum(arr[0][2],arr[1][1],arr[2][0])==3*b:
        #code for a wins
        return 1

    return 0


def not_complete(mat,ct):
    x = check_win(ct+1,mat)
    
    if x==1:
        #code for a wins
        return 0
    if sum(mat[0])+sum(mat[1])+sum(mat[2])==54:
        #code for DRAW
        return 0
    return 1

while not_complete():
