def caching_fibonacci():
    # Створюємо порожній словник cache
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            # Перевіряємо, чи є значення у кеші
            if n not in cache:
                # Якщо ні, додаємо розраховане значення в кеш
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci

def main():
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()
    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))
    print(fib(15)) 

if __name__ == "__main__":
    main()


