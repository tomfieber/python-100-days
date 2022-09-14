#!/usr/bin/env python3

"""
This is a silly love score calculator - Excercise for Day 3
"""

def get_names():
    name1 = input("Enter the first name: ")
    name1 = name1.lower()
    name2 = input("Enter the second name: ")
    name2 = name2.lower()
    return name1, name2

def interpret_score(score):
    if score < 10 or score > 90:
        print(f"Your score is {score}. You go together like coke and mentos!")
    elif score > 40 and score < 50:
        print(f"Your score is {score}, you're alright together.")
    else:
        print(f"Your score is {score}")

def calculate_love():
    name1, name2 = get_names()
    true_array = ['t', 'r', 'u', 'e']
    love_array = ['l', 'o', 'v', 'e']
    true_count = 0
    love_count = 0
    for name in [name1, name2]:
        for letter in true_array:
            total = name.count(letter)
            true_count += total

        for letter in love_array:
            total = name.count(letter)
            love_count += total

    love_score = str(true_count) + str(love_count)
    final_love_score = int(love_score)
    return final_love_score

def run_helper():
    score = calculate_love()
    interpret_score(score)

if __name__ == "__main__":
    run_helper()
