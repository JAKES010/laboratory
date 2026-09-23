# 1--------------------------------------------------------------------------------------------------------------------------
# from datetime import date 
# name = input("ENTER YOUR NAME: ")
# age = input("ENTER YOUR AGE: ")
# current_year = date.today().year
# year_needed = 100 - int(age)
# year_at_100 = current_year + year_needed
# print(f"Hello, {name}! You will be 100 in {year_at_100}")

# 2--------------------------------------------------------------------------------------------------------------------------------
# numbers = [4, 8, 15, 3, 16, 87, 23, 42]
# total = 0
# average = 0
# smallest = numbers[0]
# largest = numbers[0]
# for num in numbers:
#     if num:
#         total += num
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# average = total / len(numbers)

# print(f"SUM: {total}")
# print(f"AVERAGE: {average}")
# print(f"MAX: {largest}")
# print(f"MIN: {smallest}")

# 3------------------------------------------------------------------------------------------------------------------------------------------------
# def is_even(num):
#     if num % 2 != 0:
#         return False
#     else:
#         return True

# print(is_even(6))
# print(is_even(3))
# print(is_even(9))
# print(is_even(4))
# print(is_even(7))
    
# 4------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# for num in range(1, 51):
#     if num % 5 == 0 and num % 3 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# 5---------------------------------------------------------------------------------------------------------------------------------------------------------
# def is_prime(n):
#     if n < 2:
#         return False
    
#     for num in range(2, n):
#         if n % num == 0:
#             return False
#     return True

# print(is_prime(7))  
# print(is_prime(1))    
# print(is_prime(4))   
# print(is_prime(17))  

#6----------------------------------------------------------------------------------------------------------------------------------------------------------------
# def rowwer(n):
#  for row in range(1, n + 1):
  