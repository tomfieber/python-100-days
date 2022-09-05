#!/usr/bin/env python3

"""
This is a simple tip calculator for Day 2 of 100-days-of-code in Python
"""

def get_values():
    bill = input("How much was the bill?")
    if bill.startswith('$'):
        bill_as_float = bill.lstrip('$')
        bill = round(float(bill_as_float), 2)
    else:
        bill = round(float(bill), 2)

    while True:
        tip = input("How much of a tip do you want to leave? 12%, 15%, or 20%")
        if tip not in ['12', '15', '20']:
            print("Try again")
            continue
        else:
            break
    percentage = int(tip) / 100

    parties = input("How many people are splitting the bill?")
    number_of_parties = int(parties)

    return bill, percentage, number_of_parties

def calculate_tip():
    bill, tip_pct, number_of_parties = get_values()
    tip_value = bill * tip_pct
    total_bill = bill + tip_value
    party_split = round((total_bill / number_of_parties), 2)
    print(f"Each person should pay ${party_split}")


if __name__ == "__main__":
    calculate_tip()