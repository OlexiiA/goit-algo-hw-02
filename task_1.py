# Завдання 1: імітація обробки заявок у сервісному центрі.

from itertools import count
from queue import Queue


queue = Queue()
request_numbers = count(1)


# Створює заявку з унікальним номером і додає її до черги.
def generate_request():
    request = next(request_numbers)
    queue.put(request)
    print(f"Створено та додано до черги заявку №{request}.")
    return request


# Обробляє найстарішу заявку або повідомляє про порожню чергу.
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Оброблено заявку №{request}.")
        queue.task_done()
        return request

    print("Черга заявок порожня.")
    return None


def main():
    print("Сервісний центр: приймання та обробка заявок.")

    try:
        while True:
            generate_request()
            process_request()

            command = input("Enter — продовжити, q — вийти: ").strip().lower()
            if command == "q":
                break
    except (KeyboardInterrupt, EOFError):
        pass

    print("\nРоботу сервісного центру завершено.")


if __name__ == "__main__":
    main()
