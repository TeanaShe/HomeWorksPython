number = list(input())
mult_digits =int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
number.sort()

print("multiplying of 4 digits is {} ".format(mult_digits))
print("reverse number is ",number[3], number[2], number[1], number[0], sep='')
print("sorted digits are ", *number, sep='')


#number = int(input())
#digit4 = number % 10
#digit3 = (number // 10) % 10
#digit2 = (number // 100) % 10
#digit1 = (number // 1000) % 10
#my_digits = [digit1, digit2, digit3, digit4]
#multi_digits = digit1 * digit2 * digit3 * digit4
#digits_reverse = digit4*1000 + digit3*100 + digit2*10 + digit1
#my_digits.sort()
#print("multiplying of 4 digits is {} ".format(multi_digits))
#print("reverse number is {}".format(digits_reverse))
#print("sorted digits are {}".format(*my_digits))
