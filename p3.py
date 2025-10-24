#Exercise 3
#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
#  and makes a new list of only the first and last elements of the given list.
#  For practice, write this code inside a function.


def my_newlist(a):  
    mylist = [a[0],a[-1]]
    return mylist

P =[5,20,25,30,65,201,2]
print(my_newlist(P))