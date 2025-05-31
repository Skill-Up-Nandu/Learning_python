# Flatten a 3D list
# ➤ Given matrix = [[[1, 2], [3, 4]], [[5, 6],[7,8]], create a flat list: [1, 2, 3, 4, 5, 6]

three_d_list = [[[1, 2], [3, 4]], [[5, 6],[7,8]]]
print('3D List :',three_d_list)

# stepwise flattening 3d -> 2d -> 1d
flatted_2d =[item for sublist in three_d_list for item in sublist]
flatted_1d = [ item for sublist in flatted_2d for item in sublist]
print('Flatted 3D (stepwise):',flatted_1d)

# flatten 3d list directly
direct_3d = [item for sublist in three_d_list for subsublist in sublist for item in subsublist]
print('flatten 3D (direct):',direct_3d)
