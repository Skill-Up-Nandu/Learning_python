# IDENTITY OPEARTORS

# IS : Returns True if both variables point to the same object in memory.

a = [1,2,3]
b = a
print(a is b)

# IS NOT : Returns True if both variables do not point to the same object.

a = [1,2,3]
b = [1,2,3]
print(a is not b)

#   == : both variables are equal
#   is not : both variables refers the same objects

# practical use

x = None
if x is None:
    print(f"X is {x}.")