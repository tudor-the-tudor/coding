for numbers in range(1, 1001):
    for i in range(2, numbers):
        if numbers % i == 0:
            break
    else:
        print(numbers)