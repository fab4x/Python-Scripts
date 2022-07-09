#python script for a vending machine

#import lib to pause and to measure the time between start and end
import time

#array with products - extend as you please
fruits = ['1. Snickers', '2. Mars', '3. Doritos']

while True:
    try:
        start = int(time.time())

        print("Please select one of the Snacks listed below\n")
        print("\n".join(fruits))

        choice = int(input())
        cfruit = choice - 1

        chose = fruits[cfruit]
        print(chose + "\n")
        end = int(time.time())
        print(end - start)
        print("Please wait until the machine is ready again!")
        time.sleep(10)

        pass
    except ValueError:
        print("Please enter a valid number!\n")
    except IndexError:
        print("This number is not included in the list\n")
