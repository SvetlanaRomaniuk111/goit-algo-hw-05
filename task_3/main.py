import sys
from typing import List, Dict

def parse_log_line(line: str) -> Dict[str, str]:
    """Парсить рядок логу і повертає словник з розібраними компонентами."""
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return {}  # Повертаємо порожній словник для некоректних рядків
    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level.upper(),  # Перетворюємо рівень на верхній регістр
        "message": message
    }

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """Читає лог-файл і повертає список словників з компонентами логу."""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """Фільтрує лог-записи за заданим рівнем логування."""
    level = level.upper()  # Перетворюємо рівень на верхній регістр для порівняння
    logs_by_level = [log for log in logs if log["level"] == level]
    return logs_by_level

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """Підраховує кількість записів для кожного рівня логування."""
    log_counts = {}
    for log in logs:
        level = log["level"]
        log_counts[level] = log_counts.get(level, 0) + 1
    return log_counts

def display_log_counts(counts: Dict[str, int]):
    """Форматує і виводить результати підрахунку."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def display_log_details(logs: List[Dict[str, str]], level: str):
    """Виводить деталі логів для вказаного рівня логування."""
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python task_3/main.py task_3/logfile.log рівень_логування")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    # Завантажуємо лог-файл
    logs = load_logs(log_file_path)

    # Підраховуємо кількість записів за рівнями
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    # Якщо заданий рівень логування, фільтруємо і виводимо відповідні записи
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            display_log_details(filtered_logs, log_level)
        else:
            print(f"\nЗаписи з рівнем {log_level.upper()} не знайдено.")

if __name__ == "__main__":
    main()
