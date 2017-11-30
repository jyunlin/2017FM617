def multiplication_table(m,n):
    for i in range(1,10):
        for j in range(m,n+1):
            print(('%sX%s=%s\t') % (j,i,i*j),end='')
        print("");
    print("");

def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))
