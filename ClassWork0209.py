def aver_arif(*args):
    """Function for arifmetic average"""
    total = 0
    cnt = 0
    for num in args:
        total += num
        cnt += 1
    return total / cnt

def max_num(first, second):
    """Function for max number from 2 numbers"""
    if first >= second:
        return first
    else:
        return second

PI = 3,14

n = int(input('''Hi, if you want to calculate the area of the triangle enter 1.
If you want to calculate the area of the rectangle - enter 2.
And if you want to know the area of the circle - enter 3. So choose your number '''))


def area_triange(a, b, c):
    """Area of the triange"""
    p = a + b + c
    S = round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)
    return S 


def area_rectangle(a, b):
    """Area of the rectangle"""
    S = round(a * b, 2)
    return S


def area_circle(r):
    """Area of the circle"""
    S = PI * (r**2)
    return S


if n == 1:
    figure = "triangle"
    a, b, c = (int(i) for i in input("Enter sides of the triangle ").split())
    S = area_triange(a, b, c)
elif n == 2:
    figure = "rectangle"
    a, b = (int(i) for i in input("Enter sides of the rectangle ").split())
    S = area_rectangle(a, b)
elif n == 3:
    figure = "circle"
    r = int(input("Enter the radius of the circle "))
    S = area_circle(r)
else:
    print("You didn't make a right choise")
print(f'The area of the {figure} is {S}')


def count_symbols(string):
    """Counting symbols in the string"""
    my_tuple_full = tuple(''.join(string.split()))
    my_dict = {symbol: my_tuple_full.count(symbol) for symbol in my_tuple_full}
    return my_dict

    