def add_one(digits: list) -> list:
    """
    Приймає список цифр, перетворює їх на число, додає 1
    і повертає результат як список цифр.
    """
    number_str = ''.join(map(str, digits))

    number = int(number_str) + 1

    return [int(i) for i in str(number)]


if __name__ == "__main__":
    print(add_one([1, 2, 3, 4]))
    print(add_one([9]))
    print(add_one([9, 9, 9]))
    print(add_one([0]))