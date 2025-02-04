def lalala() -> None:
    p = int(input("Введи число: "))
    square = {}
    
    for i in range(1, p + 1):
        square[i] = i ** 2
    
    print(square)

lalala()
