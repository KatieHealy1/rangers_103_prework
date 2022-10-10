# Write a function to print "Hello_User"
def hello_name(user_name):
    """Display greeting"""
    print("\nHello " + user_name + ".")

hello_name('Katie')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for number in range(1,101):
        if number % 2 == 1:
            print(number)

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])

max_num_in_list([1,3,5,6,7,9,8])

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false)

def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0): 
        return True
    elif (a_year % 100 == 0) and (a_year % 400 != 0):
      return False
    else:
      leap = False
      return False

print(is_leap_year(2024))


# Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. 


def is_consecutive(a_list):
    min_value = min(a_list)
    max_value = max(a_list)
    a_list.sort()
    for number in a_list:
        if number == min_value:
            min_value += 1
        else:
            return False
        last_number = number
    if last_number == max_value:
        return True
    else:
        return False
a_list = [1, 2, 3, 4, 5, 6]
print(is_consecutive)
