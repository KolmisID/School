def element(numbers):
    return sum(numbers)

numbers = list(map(int, input("Введи число: ").split()))

result = element(numbers)

print("Сума всіх: ", result)
