# UNPACK WITH * OPERATOR
# t = (1, 2, 3, 4, 5)
# Unpack the first element into a, the rest into b

t = (1, 2, 3, 4, 5)
print(f"Tuple : {t}")

# unpack using * operator
a , *b = t
print(f"a : {a}")
print(f"b : {b}")