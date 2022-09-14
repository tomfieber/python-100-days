#!/usr/bin/env python3

import sys


def banner():
    print('''
                      ,,
         ,,       ,\\//,
       ,\\//,    ,\\\///,   ,,
      ,\\\///,   \\\\//// ,\\//,
      \\\\////    \\\/// ,\\\///,
       \\\///     ###### \\\\////
       ######    ////\\\\ \\\///
      ////\\\\  /////\\\\\######
     /////\\\\\//////\\\\////\\\\
    //////\\\\\\/,///\\\/////\\\\\
   //////_?_\\\\(_)    //////\\\\\\,
      .'`---`'.    _j_///////\\\\\(_)
     /.'a   a  \.'`---`'.
     |:   ^    /.'d\ /b  \\
     \'  www   |:   ^     |
      '._____.'\'  VVV    /
  jgs           '._____.'
  ''')
    print("Welcome to my Pumpkin Patch!!")
    print("Your mission is to find the Great Pumpkin...")
    print("...But you'll have to navigate a giant corn maze to get to the pumpkin patch and the Great Pumpkin.")
    print("Good luck!")


def third_challenge():
    print("Weird...three crudely painted wooden doors have appeared in the wall of the maze. How did you miss those?")
    choice = input("Which door would you like to go through? (red/yellow/blue)")
    choice = choice.lower()
    if choice == 'yellow':
        print("You found the pumpkin patch and the Great Pumpkin!!")
    elif choice == 'red':
        print("Well, you walked straight into an inferno and your face has melted off. Game over.")
        sys.exit()
    else:
        print("You have chosen poorly...you've been devoured by beasts. Bummer.")
        sys.exit()


def second_challenge():
    print("It looks like the corn maze backs up to a lake and continues on the other side.")
    swim = input("Do you want to swim, or backtrack to see if you missed something? (swim/back)")
    swim = swim.lower()
    if swim == 'swim':
        print("You are attacked by a huge school of trout. They quickly overwhelm you, and you succumb to their vicious attack. Sorry")
        sys.exit()
    elif swim != 'back':
        print("You've waited too long, and the maze has consumed you. This is not a nice place.")
        sys.exit()
    else:
        print("Alright")
        third_challenge()


def first_challenge():
    direction = input("You come to the first wall in the corn maze. Do you want to go left or right? (L/R)")
    direction = direction.lower()
    if direction == 'left' or direction == 'l':
        print("Ok, so far so good...")
        second_challenge()
    else:
        print(
            "You fell into a hole and have broken both your legs.You should just come to grips with the fact your going to die here. Sorry.")
        sys.exit()


def run():
    first_challenge()


if __name__ == '__main__':
    banner()
    run()
