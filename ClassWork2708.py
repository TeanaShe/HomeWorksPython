"""Max number from many numbers"""

# n = int(input("how many numbers will be? "))
# my_list = []
# for i in range (n):
#     m = int(input('enter number '))
#     my_list.append(m)
# print(f"The maximum number in the list is {max(my_list)}")
# print(f"The minimum number in the list is {min(my_list)}")

"""eval and odd numbers"""

# eval_numbers = []
# odd_numbers_mult3 = []
# odd_numbers_not_mult3 = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         eval_numbers.append(i)
#     elif i % 3 == 0:
#         odd_numbers_mult3.append(i)
#     else:
#         odd_numbers_not_mult3.append(i)        
# print(f"Eval numbers in the range(1-10) are:", (eval_numbers))
# print(f"Odd numbers in the range(1-10) mult.3 are: {odd_numbers_mult3}")
# print(f"Odd numbers in the range(1-10) not mult.3 are: {odd_numbers_not_mult3}")

"""Simple factorial"""

# n = int(input("Enter your number: "))
# i = 1
# fact_n = 1
# while i <= n:
#     fact_n *= i
#     i += 1
# print(f"{n}! = {fact_n}")


"""Calculation factorial by recursive function"""

# def calc_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * calc_factorial(n-1)

# print(calc_factorial(5))



"""Checking login"""

# login = input('Please, enter your login: ')
# while login != 'First':
#     print('Error! Retry your login')
#     login = input('Your login: ')
# print(f'Hello, {login}!')