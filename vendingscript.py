#python script for a vending machine

#import lib to pause and to measure the time between start and end
import time

#array with products - extend as you please
snacks = ['1. Snickers', '2. Mars', '3. Doritos']
#array with prices 
prices = ['5']

while True:
    try:
        start = int(time.time())

        print("Please select one of the Snacks listed below\n")
        print("\n".join(snacks))

        choice = int(input())
        csnack = choice - 1

        chose = snacks[csnack]
        print(chose + "\n")
        end = int(time.time())
        print(end - start)
        print("Please wait until the machine is ready again!")
        time.sleep(10)
        
    #if input is not a int value - this error will be printed
    except ValueError:
        print("Please enter a valid number!\n")
    #if input int value is higher than a index number in array - this error will be printed
    except IndexError:
        print("This number is not included in the list\n")
