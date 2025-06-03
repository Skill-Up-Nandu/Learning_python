# SWAP TWO VARIABLES
# a = 5
# b = 10
# Use tuple unpacking to swap their values

a = 5
b = 6
print("\nBefore Swapping : ")
print(f"a : {a}")
print(f"b : {b}")

print("\n===============================\n")

# swapping using tuple unpacking (no temp variable needed)
a , b = b , a
print("After Swapping : ")
print(f"a : {a}")
print(f"b : {b}")

