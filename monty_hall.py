# Monty Hall Problem Simulator
# Jason Kennerdell
# 8/11/15


print("This program simulates and tabulates the results of various Monty Hall Problems.")

### Get the parameters that the user wants to use in the simulation

initial_doors = int(input("How many doors would you like to start out with?"))

opened_doors = int(input("How many of these doors should Monty open?"))

#switch = int(input("Press 1 if you are a switcher, or press 2 if you are a stayer"))

iterations = int(input("How many simulations would you like to run?"))
                   

# define variables
number_of_switches = 0
number_of_stays = 0
switch_success = 0
switch_failure = 0
stay_success = 0
stay_failure = 0
switch = 0


# import the random module

import random

# set up iterations loop
for i in range(0, iterations):
    # assign a door as the prizewinner
    prize = random.randint(1, initial_doors)
    # assign a guess at random
    guess = random.randint(1, initial_doors)
    # Monty opens doors
    revealed = []
    revealed_test = 0
    for j in range (0, opened_doors):
                   unacceptable_reveals = [prize, guess, 0] + revealed
                   while revealed_test in unacceptable_reveals:
                       revealed_test = random.randint(1, initial_doors)
                   revealed = revealed + [revealed_test]
    #print("\n", prize, guess, revealed)
    # randomly assign switch or not switch
    switch = random.randint(1, 2)
    if switch == 1:
        number_of_switches += 1
        # Switch to another door
        second_guess = guess
        while second_guess == guess or second_guess in revealed:
            second_guess = random.randint(1, initial_doors)
        if second_guess == prize:
            switch_success += 1
        else:
            switch_failure += 1
    if switch == 2:
        number_of_stays += 1
        if guess == prize:
            stay_success += 1
        else:
            stay_failure += 1

if number_of_switches > 0:
    switch_success_rate = 100 * switch_success / number_of_switches
else:
    switch_success_rate = 0
if number_of_stays > 0:
    stay_success_rate = 100 * stay_success / number_of_stays
else:
    stay_success_rate = 0
    
print("You have run", iterations, "iterations.")

print("You started with", initial_doors, "doors, and Monty opened", opened_doors, "of those doors which did not have the prize.")

print("Switching occured", number_of_switches, "times, and was successful", switch_success, "times. The success rate was", switch_success_rate, "percent.")

print("Staying occured", number_of_stays, "times, and was successful", stay_success, "times. The success rate was", stay_success_rate, "percent.")

        
        
        
       
        

