# Flatten a 2D list
# ➤ Given matrix = [[1, 2], [3, 4], [5, 6]], create a flat list: [1, 2, 3, 4, 5, 6]

two_d_list = [[1, 2], [3, 4], [5, 6]]

# print the all items of list
flatted = [item for item in two_d_list]
print('Original List : ',flatted)

# print 2d list as fattern
flatted_2d = [item for sublist in two_d_list for item in sublist]
print('flatted List :',flatted_2d)
