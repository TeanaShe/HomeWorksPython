#for number in range (101):
#    if number % 2 == 0:
#        print(number)

#number = 0
#while number < 101:
#    if number % 2 == 0:
#        print(number)
#    number += 1


for i in range(101):
    if i % 2 == 0:
        continue
    print(i)

print(*list(range(1, 100, 2)))

list_number = [2,4,6,8,9,10]
contain_odd = False
for item in list_number:
    if not item % 2 == 0: 
        contain_odd=True
        break
if contain_odd:
    print("There is odd number in the list")
else: 
    print("There is only even number in the list")

my_list = [1,3,8,23,11,34]
for i in range(len(my_list)):
    my_list[i] = float(my_list[i])
print(my_list)


n = int(input())
fib1 = 0
fib2 = 1
print(fib1)
print(fib2)
while (fib1 + fib2) <= n:
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2)
