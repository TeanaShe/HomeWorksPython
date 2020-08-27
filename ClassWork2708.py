n = int(input("how many numbers will be? "))
my_list = []
for i in range (n):
    m = int(input('enter number '))
    my_list.append(m)
print(f"The maximum number in the list is {max(my_list)}")
print(f"The minimum number in the list is {min(my_list)}")
