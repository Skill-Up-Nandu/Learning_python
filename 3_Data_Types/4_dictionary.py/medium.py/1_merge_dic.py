# update two dictionaries
# tip -> if both the dictionaries have the same key , the value from the second dictionary will be overwrites the value from the fist .


sec_a = {
    "topper_name" : "Anant" ,
    "roll_no" : 425 ,
    "marks" : 98.5 
}

sec_b = {
    "topper_name" : "Nikita" ,
    "roll_no" : 236 ,
    "marks" : 96.8 
}

# it modifies the first one
def update_dic(dic_1 , dic_2 ) :
    dic_1.update(dic_2)
    print(f"\nUpdate Method (overwrites the key's value)\n")
    for idx ,(k , v) in enumerate(dic_1.items() , 1) :
        print(f"{idx}. {k.title()} : {v}")

# creates another merged dictionary
def merge_dic(dic_1 , dic_2) :
    merged = dic_1 | dic_2
    print(f"\nMerged Method '|'\n")
    for idx,  (k , v) in enumerate(dic_1.items() , 1) :
        print(f"{idx}. {k.title()} : {v}")


# using dictionary unpacking
def unpack_dic(dic_1 , dic_2) :
    merged = {**dic_1 , **dic_2}
    print(f"\nUnpack Dictionary '**': \n")  
    for idx , (k , v) in enumerate(dic_1.items() , 1) :
        print(f"{idx}. {k.title()} : {v}")
  

# second dic will overwrite the first one
update_dic(sec_a , sec_b) 

section_a = {
    "topper_sec_a" : "Anant" ,
    "roll_no_sec_a" : 425 ,
    "marks_sec_a" : 98.5 
}

section_b = {
    "topper_name_sec_b" : "Nikita" ,
    "roll_no_sec_b" : 236 ,
    "marks_sec_b" : 96.8 
}

# key's name should be unique for both the dictionary to avoid overwritten items
update_dic(section_a , section_b) 

merge_dic(section_a , section_b) 

unpack_dic(section_a , section_b)