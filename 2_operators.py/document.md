# Types of Operators in Pyhton

# Arithmetic Operators
    1. add +
    2. sub -
    3. mul *
    4. div /   # always results the float value
    5. int div //  # it works as floor wich retuns th smallest integer value (but written as float)
    6. modulo %   # returns the remainder after division (returns negative value if only the divisor is negative )
    7. power **   # return the power of a value 2**3 == 8

# Comparison Operators
    1. equal ==
    2. not equal !=
    3. greater than >
    4. less than <
    5. greater than or equal to >=
    6. less than or equal to <=
    # you must try clever if statements to understand the comparison operators better

# Logical Operators

**Logical operators in Python are used to perform logical operations on conditional statements. They are mainly used in control flow statements like if, while, and in filtering data.**

**User has to answer in "yes" or "no" but logically i want to store it in "true" or "false".**
code ~
    user_input = input("Do you agree? (yes/no): ").strip().lower()
    is_agreed = True if user_input == "yes" else False
    print("Boolean value:", is_agreed)

    1. and
    2. or
    3. not

# Assignment Operators

**Assignment operators in Python are used to assign values to variables. Python supports a variety of assignment operators that help modify and assign values efficiently.**  

    1. =  # assignment
    2. += # add and assign
    3. -= # subtract and assign
    4. *= # multiply and assign
    5. /= # divide and assign
    6. %= # modulo and assign
    7. //= # int div and assign
    8. **= # power and assign

# Identity Operators

**Identity operators in Python are used to compare the memory location of two objects. They check whether two variables point to the same object in memory (not just if their values are equal).**

    1. is
    2. is not

# Membership Operators

**Membership operators in Python are used to test whether a value or variable is present in a sequence (like string, list, tuple, set, or dictionary).**

    1. in
    2. not in   
# Bitwise Operators

**Bitwise operators perform operations on the binary representations of integers. They operate bit by bit, which means they treat numbers as a sequence of bits (0s and 1s) rather than decimal or other representations.**

    **Prefix - 
        *0b - binary
        *0x - hexadecimal
        *0o - octal

    1. &  # bitwise AND
    2. |  # bitwise OR
    3. ^  # bitwise XOR
    4. ~  # bitwise NOT
    5. << # left shift
    6. >> # right shift
# FACTS 

#no.1 
    If you want a positive value use abs() .