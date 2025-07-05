# Given a dictionary of item prices and a list of items bought, calculate the total cost.

prices = {'apple': 10, 'banana': 5, 'orange': 8}
cart = ['apple', 'banana', 'apple', 'orange', 'banana']

def cal_cost():
    bill = {}
    for item in cart :
        bill[item] = bill.get(item , 0 ) +  prices.get(item)
    total_cost = sum(bill.values())
    print(f"Total cost spent : {total_cost}")
    return bill

def get_bill(bill):
    print("\n------------------------------------------------\n")

    print(f"2025-05-07\t\t\tBill_no : 7854\n")
    print(f"\tSr_No\tItem\tPrice")
    print(f"\t---------------------")

    for idx , (k , v) in enumerate(bill.items() , 1) :
        print(f"\t{idx}.\t{k}\t{v}")

    print(f"\t---------------------")
    print(f"\tTotal Cost\t{sum(bill.values())}")
    print(f"\t---------------------\n")

bill = cal_cost()
get_bill(bill)

