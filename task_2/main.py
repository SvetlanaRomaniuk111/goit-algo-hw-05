import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Регулярний вирази для ідентифікації дійсних чисел відокремлених пробілами
    pattern = r"\s\d+\.\d+\s"
    # Знаходимо всі збіги шаблону
    numbers = re.findall(pattern, text)
    # Перетворюємо кожен знайдений елемент на float і повертаємо через yield
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]) -> float:
    # Використання генератора для обчислення загальної суми
    return sum(generator_numbers(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Обчислення загального доходу за допомогою функції sum_profit
total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")

#-- якщо дані знаходяться в окремому файлі text.txt -----------

import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # 
    # Знаходимо всі збіги шаблону в тексті
    numbers = re.findall(pattern, text)
    # Перетворюємо кожен знайдений елемент на float і повертаємо через yield
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]) -> float:
    # Використання генератора для обчислення загальної суми
    return sum(generator_numbers(text))

def num_counter(filename: str) -> None:
    # Відкриття файлу і зчитування його вмісту
    with open(filename, 'r') as file:
        text = file.read()
        # Обчислення загального доходу за допомогою функції sum_profit
        total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

# Виклик функції num_counter для обчислення доходу з файлу 'text.txt'
num_counter('task_2/text.txt')
