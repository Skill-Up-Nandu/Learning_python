# bitwise operators

# we should write 0b as prefix to any binary number (facts)

# AND
a = 0b1010
b = 0b1100
c = a & b
print(f"\nAND of {a} & {b} ->")
print(f"C : {bin(c)} | {c}\n")

# OR
d = a | b
print(f"OR of {a} | {b} ->")
print(f"D : {bin(d)} | {d}\n")

# XOR
e = a ^ b
print(f"XOR of {a} ^ {b} ->")
print(f"E : {bin(e)} | {e}\n")

# <<
digit = 0b1100
f = digit << 2
print(f"LEFT SHIFT of {digit } ->")
print(f"F : {bin(f)} | {f}\n")

# >>
digit = 0b1100
f = digit >> 2
print(f"RIGHT SHIFT of {digit} ->")
print(f"F : {bin(f)} | {f}\n")

# ~
num = 0b1000
g = ~num
print(f"NOT(complement) of {num} ->")
print(f"G : {bin(g)} | {g}\n")