#python script for a vending machine
#it can only handle one item at the time.

#import library to pause and to measure the time between start and end
import time

#array with products - extend as you please
snacks = ['1. Snickers', '2. Mars', '3. Doritos']
#array with prices 
prices = ['2.50', '2.00', '3.00']
#array with amount in store
storage = [10, 5, 1]

def calc():
    for i in range(len(storage)):
        if i < 1:
            storage.pop(i)
            snacks.pop(csnack)


#try and catch to avoid an unplanned exit
while True:
    try:
        #start of the programm
        start = int(time.time())

        print("Please select one of the Snacks listed below\n")
        print("\n".join(snacks))

        choice = int(input())
        #calculate index position
        csnack = choice - 1

        chose = snacks[csnack]
        #calculate new item count
        amount = storage[csnack] - 1
        #set new item count in array
        storage[csnack] = amount
        #print array with new amount of items
        print(storage)
        
        # if amount < 1 return error and pop item out of list
        #for i in range(len(storage)):
         #   if i < 1:
          #     print(i)
           #     storage.pop(i)

        #call function calc
        calc()  
        #print the array with the amount of items left
        print(amount)
        print(chose + "\n")
        #end of the programm
        end = int(time.time())
        #print(end - start)
        print("Please wait until the machine is ready again!")
        #wait for 10 seconds until machine is ready again
        #time.sleep(10)
        
    #if input is not a int value - this error will be printed
    except ValueError:
        print("Please enter a valid number!\n")
    #if input int value is higher than a index number in array - this error will be printed
    except IndexError:
        print("This number is not included in the list\n")