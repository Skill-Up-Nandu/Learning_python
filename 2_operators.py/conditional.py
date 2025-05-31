# FACT - first you have the knowledge of conditional statements!

print("Conditional operators are like nosy relatives — constantly asking, 'Are you two really equal (==)? Is he older (>)? Is she younger (<)? Or should we just break this off (!=)?")

print(" Enter Details : ")
print("user 1: ")
user1 = input("Name : ")
age1 = int(input("Age : "))
print("user 2: ")
user2 = input("Name: ")
age2 = int(input("Age : ")) 
print("\n****************************************************************************")
print("Frenship Status: ")
if age1 == age2:
    print(user1, "and", user2, "you both are basically twins, but from different parents.")
elif age1 > age2:
    print(user1," is older.",user2," Respect your elders… unless they steal your fries!")
elif age1 < age2:
    print(user1, "is younger. Fresh brain, fewer regrets!")
else:
    print("Time warp detected! Please check your ages again.")

print("\nThanks for understanding you freindship status! Now you can enjoy your time together without any confusion. Remember, age is just a number, but friendship is forever! 💖")