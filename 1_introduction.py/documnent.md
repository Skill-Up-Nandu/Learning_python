# What is Python ? 
    1. Developed by "GUIDO VAN ROSSUM".
    2. Pyhton is simple and easy language.
    3. DYnamic language.
    4. Free and Open source.
    5. High level language.
    6. Portable Langauge.

# FILE EXTENSION : ".py"

# Input/Output : 
To take input from user : input() // string by default
To take any another type of data as input " we have to typecast the input() statement "
    for int - int(input()) and so on.... 

# string method
Whenever we asked for an userinput in the form of string we should add some method such as ".strip()" -> to remove extra space and ".lower()/.upper()/.title()" to change the text into required case. 

# Data types in python :
    > Python supports following data types-
        1.Test
            *str (default)
        2.Numerical
            *int
            *float
            *complex
        3.Sequence
            *list
            *tuple
            *range
        4.Mapping
            *dict(dictionery)
        5.Boolean
            *bool
        6.Binary 
            *bytes
            *bytearray
            *memoryview
        7.Void
            *none
    
# Facts 

# No 1(bool input)
    1. Bool : In bool() , every non-empty string is considers as True // no matter you type true/false .
            want actual boolean value as result.
            try:
            a = bool(input("True/False : "))
            answer = a == "True"
            print(answer)
            //if else concept
                if (a == True): only then answer will return True , otherwise (false or any other string) False will return as answer.