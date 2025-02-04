def cookie() -> None:
    number = int(input("Введіть число: "))
    if number % 2 == 0:
        print(f"{number} число парне.")
    else:
        print(f"{number} число непарне.")

cookie()
