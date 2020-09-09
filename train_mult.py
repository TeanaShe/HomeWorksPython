def solution(number):
    total = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total
