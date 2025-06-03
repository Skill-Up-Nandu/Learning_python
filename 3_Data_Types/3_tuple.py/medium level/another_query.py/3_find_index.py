# Find Index
# Find the index of "blue" in this tuple:
# colors = ("red", "green", "blue", "yellow")

colors = ("red", "green", "blue", "yellow")
print("All Colors : ", colors)

# manual appoach
for idx , color in enumerate(colors):
    if color == 'blue':
        print("\nGet Index by using mannual approach :")
        print(f"Color 'blue is at '{idx}' index")
        break

# using built-in function
index = colors.index('blue')
print("\nGet Index by using built-in function :")
print(f"Color 'blue is at '{index}' index")