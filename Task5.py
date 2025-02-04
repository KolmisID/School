def ticket_sells() -> None:
    a_tickets = int(input("Тікетів продано в класі А: "))
    b_tickets = int(input("Тікетів продано в класі В: "))
    c_tickets = int(input("Тікетів продано в класі С: ")) 

    a_price = int(input("Ціна в класі А: "))
    b_price = int(input("Ціна в класі В: "))
    c_price = int(input("Ціна в класі С: "))

    a_sells = a_tickets * a_price
    b_sells = b_tickets * b_price
    c_sells = c_tickets * c_price
    total_sells = a_sells + b_sells + c_sells

    print(f"{a_sells}\n{b_sells}\n{c_sells}\n{total_sells}")

ticket_sells()
