import numpy as np 

s = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

row_sum = np.sum(s,1)
# print(row_sum)
col_sum = np.sum(s,0)
# print(col_sum)
block_sum = []
# print(type(block_sum))

for i in row_sum :
    if i != 45 :
        print("Invalid Sudoku")
        break
else :
        print("Valid for rows")

for i in col_sum :
    if i != 45 :
        print("Invalid Sudoku")
        break
else :
        print("Valid for columns as well")  

# part_s = s[:3,:3].sum()
# print(part_s)

# if s[:3,:3].sum() == 45 and s[:3,3:6].sum() == 45 and s[:3,6:].sum() == 45 :
#      print("first block is also valid")

# loop for rows
for i in range(0,9,3) :
    #  loop for columns
     for j in range(0,9,3) :
        #   print(s[i:i+3,j:j+3])
        n = s[i:i+3,j:j+3].sum()
        block_sum.append(n)
# print(list(block_sum))
for i in block_sum :
     if i != 45 :
          print("Invalid Sudoku block wise")
else : print("Valid Sudoku Block Wise as Well")