





#Question1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.




def hello_name(user_name):
    print("hello_"+user_name+"!")

#hello_name(input("what is your name?  "))


#Question 2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for num in range(1,101):
        if num%2 == 1:
            print(num)



#first_odds()


#Question 3 Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    stored_num = a_list[0]
    for num in a_list:
        if num > stored_num:
            stored_num=num
    return(stored_num)

#print(max_num_in_list([1, 16, 24, 32, 21, 108, 12, 11]))

#Question 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    int_year = int(a_year)
    if int_year%4 == 0 and int_year%100 != 0:
        leap = True
    elif int_year%400 == 0:
        leap = True
    else:
        leap = False
    return(leap)

#print(is_leap_year(input("Enter a year?  ")))

#Question 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    i = 0
    consecutive = True
    for num in a_list:
        if i == 0:
            stored_num = num
            i = i+1
            continue
        if num != stored_num+1:
            consecutive=False
            break
        stored_num = num
    return(consecutive)

#print(is_consecutive([1, 2, 3, 8, 5, 6]))
#print(is_consecutive([1, 2, 3, 4, 5, 6]))



    





