# n = input('enter your number')

# try:
#     if n % 2 == 0:
#         print(f'{n} is even')
#     else:
#         print(f'{n} is odd')
# except ValueError as e:
#     print('Error is: ', e)
# except TypeError as e:
#     print('Error is: ', e)

"""first variant"""
# num_1, num_2 = eval(input('enter your numbers using comma: '))
#     divide_res = num_1 / num_2

"""second variant"""
# numb_list = input('enter your numbers using comma: ').split(',')

# try:
#     print('divide of 2 numbers is:', (int(numb_list[0]) // int(numb_list[1])))
# except ValueError as e:
#     print('Error: ', e)
# except TypeError as e:
#     print('Error: ', e)
# except ZeroDivisionError as e:
#     print('Error: ', e)
# except:
#     print('Input error :(')
# else:
#     print('Its OK')
# finally:
#     print('The end')


# names = ['Sam', 'Don', 'Daniel'] 
# hash_names = map(lambda names: hash(names), names)
# print(list(hash_names))


# my_list = ['1', '2', '3', '4', '5', '7']
# new_list = []
# for i in my_list:
#     new_list.append(int(i))
# print(new_list)

# new_list = list(map(int, my_list))
# print(new_list)

# my_km = [1, 2, 6]
# my_miles = list(map(lambda km: round(km * 1.6, 2), my_km))
# print(my_miles)


# from functools import reduce
# my_list = [2, 5, 1, -3]
# max_elem = reduce(lambda a, b: a if (a > b) else b, my_list)
# print(max_elem)


# colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
# print(list(filter(lambda x: x=='red',colors)))


# def my_range(first, fin, step = 1):
#     while first < fin:
#         yield first
#         first += step

# val = my_range(2, 18, 3)
# next(val)


def my_range(fin, first = 0, step = 1):
    while first < fin:
        yield first
        first += step

val = my_range(18, 3)
next(val)



