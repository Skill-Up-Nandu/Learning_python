# Flatten a 2D list
# ➤ Given matrix = [[1, 2], [3, 4], [5, 6]], create a flat list: [1, 2, 3, 4, 5, 6]

two_d_list = [[1, 2], [3, 4], [5, 6]]

# show the original 2d list
flatted = [item for item in two_d_list]
print('Original List : ',flatted)

# flatten the 2d list into a 1d list
flatted_2d = [item for sublist in two_d_list for item in sublist]
print('flatted List :',flatted_2d)
