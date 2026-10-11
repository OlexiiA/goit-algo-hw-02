# Завдання 2: перевірка паліндрома за допомогою двосторонньої черги.

from collections import deque


# Перевіряє рядок, ігноруючи регістр і пробільні символи.
def is_palindrome(text: str) -> bool:
    characters = deque(
        character for character in text.casefold() if not character.isspace()
    )

    while len(characters) > 1:
        if characters.popleft() != characters.pop():
            return False

    return True


def main():
    text = input("Введіть рядок для перевірки: ")

    if is_palindrome(text):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")


if __name__ == "__main__":
    main()
