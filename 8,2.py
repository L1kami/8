def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом, ігноруючи регістр та спецсимволи.
    Використовує O(n) пам'яті та часу.
    """
    processed_chars = [char.lower() for char in text if char.isalnum()]

    return processed_chars == processed_chars[::-1]


if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "0-0",
        "Python",
        "Eva, can I see bees in a cave?",
        ""
    ]

    for s in test_cases:
        print(f"'{s}' -> {is_palindrome(s)}")