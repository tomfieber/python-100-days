#!/usr/bin/env python3

import random

def get_names():
    names = input("Please enter a list of names, separated by commas.")
    name_list = names.split(',')
    return name_list

def decide_who_pays():
    names = get_names()
    payer = random.choice(names)
    print(f"{payer} is paying for the bill today!")

if __name__ == '__main__':
    decide_who_pays()

