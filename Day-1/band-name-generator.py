#!/usr/bin/env python
"""
This is the first project in the 100-days of Python code. It's a very simple band name generator.
"""

def banner():
    print("Welcome to the Band Name Generator!")

def generate_band_name():
    town = input("What is the name of the town you grew up in?")
    pet = input("What is the name of your pet?")
    print(f"Your band name could be called {town} {pet}!")

if __name__ == "__main__":
    banner()
    generate_band_name()

