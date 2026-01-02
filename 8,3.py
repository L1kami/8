from collections import Counter


def find_unique_value(some_list: list) -> int | float:
    """
    Оптимізований варіант пошуку унікального числа.
    Працює набагато швидше на великих списках.
    """
    counts = Counter(some_list)

    for number, count in counts.items():
        if count == 1:
            return number


if __name__ == "__main__":
    test1 = [1, 2, 1, 1]
    test2 = [2, 3, 3, 3, 5, 5]
    test3 = [5, 5, 5, 2, 2, 0.5]

    print(f"Test 1: {find_unique_value(test1)}")
    print(f"Test 2: {find_unique_value(test2)}")
    print(f"Test 3: {find_unique_value(test3)}")