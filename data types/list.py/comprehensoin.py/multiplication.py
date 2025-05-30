# Multiplication table pairs
# ➤ Generate all [i, j] pairs where 1 ≤ i ≤ 3 and 1 ≤ j ≤ 3.

mul_pair_list = [[i,j] for i in range(1,4) for j in range(1,4)]
print(mul_pair_list)

mul = [[[1, 1], [1, 2], [1, 3]], [[2, 1], [2, 2], [2, 3]], [[3, 1], [3, 2], [3, 3]]]

# flatten the 3d list
flat = [ i for sublist in mul for subsublist in sublist for i in subsublist]
print(flat)