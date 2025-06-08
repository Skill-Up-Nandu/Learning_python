# You have two dictionaries of items and prices. Merge them into one dictionary.

dic_1 = {
    'item_1' : 890, 'item_2' : 758, 'item_3' : 741
}
dic_2 = {
    'item_4' : 900, 'item_5' : 128, 'item_6' : 851
}

print(f"Ist dic : {dic_1}")
print(f"IInd dic : {dic_2}")
print("\nMerged :")
dic_1.update(dic_2)
