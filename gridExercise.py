# Say you have a list of lists where each value in the inner lists is a
# one-character string, like this:
#grid[0][0]
#       00   01   02   03   04   05
grid =[['.', '.', '.', '.', '.', '.'],
       ['.', '0', '0', '.', '.', '.'],
       ['0', '0', '0', '0', '.', '.'],
       ['0', '0', '0', '0', '0', '.'],
       ['.', '0', '0', '0', '0', '0'],
       ['0', '0', '0', '0', '0', '.'],
       ['0', '0', '0', '0', '.', '.'],
       ['.', '0', '0', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '.']]

for i in grid:
    for j in i:
        print(j, end=' ')
    print(j)

