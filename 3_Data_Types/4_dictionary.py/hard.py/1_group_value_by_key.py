# Given a list of dictionaries, group values by a key:
# data = [{'dept': 'IT', 'name': 'A'}, {'dept': 'HR', 'name': 'B'}, {'dept': 'IT', 'name': 'C'}]
# {'IT': ['A', 'C'], 'HR': ['B']}


data = [{'dept': 'IT', 'name': 'A'}, {'dept': 'HR', 'name': 'B'}, {'dept': 'IT', 'name': 'C'}]

def group_by_key():
    result = {}
    for item in data:
        dept = item['dept']
        name = item['name']
        result.setdefault(dept , []).append(name)
    print(f"Grouped Data : {result}")

    
group_by_key()