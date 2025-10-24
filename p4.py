#Write a function that takes an ordered list of numbers
#(a list where the elements are in order from smallest to largest) and another number. 
#The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def funct(a,b):
    for item in a:
        if item == b:
            return True
        False

list = [1,2,3,4,5,6,7,8,9,10]
b = 99


print(funct(list,b))