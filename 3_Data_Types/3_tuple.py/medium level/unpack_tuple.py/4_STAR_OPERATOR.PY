# UNPACK WITH * OPERATOR
# t = (1, 2, 3, 4, 5)

print("\nFIRST PROGRAMM :\n")
t = (1, 2, 3, 4, 5)
print(f"Ist Tuple : {t}")

# Unpack the first element into a, the rest into b
a , *b = t
print(f"a : {a}")
print(f"b : {b}")

print("\n========================================\n")

print("SECOND PROGRAMM :\n")
t2 = (10,20,30,40,50,60)
print(f"IInd Tuple : {t2}")

# # Unpack first into a, last into c, middle into b (as a list)
a, *b , c = t2
print(f"a : {a}")
print(f"b : {b}")
print(f"c : {c}")