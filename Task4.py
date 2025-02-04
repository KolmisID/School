def process_sentence() -> None:
    sentence = input("Введи текст: ")
    result = " ".join(word.capitalize() for word in sentence.split())
    print(result)

process_sentence()
