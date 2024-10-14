# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Not enough argument for the command"

    return inner

def parse_input(user_input):
    # Розбирає вхідний рядок користувача на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    # Додає новий контакт до словника контактів
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Змінює номер телефону для існуючого контакту
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    # Виводить у консоль номер телефону для заданого контакту
    name = args[0]
    if name not in contacts:
        raise KeyError   
    return contacts[name]

def show_all(contacts):
    # Виводить всі збереженні контакти з номерами телефонів
    if contacts:
        contact_list = ["Contacts list:"]
        for name, phone in contacts.items():
            contact_list.append(f"{name}: {phone}")
        return "\n".join(contact_list)
    else:
        return "Contacts not found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]: # Вихід з програми
            print("Good bye!")
            break
        elif command == "hello":         # Привітання
            print("How can I help you?")
        elif command == "add":           # Додавання нового контакту
            print(add_contact(args, contacts))
        elif command == 'change':        # Зміна існуючого контакту
            print(change_contact(args, contacts))
        elif command == 'phone':         # Пошук номера телефону за ім'ям
            print(show_phone(args, contacts))
        elif command == 'all':           # Вивід всіх контактів
            print(show_all(contacts))
        else:                            # Невідома команда
            print("Invalid command.")

if __name__ == "__main__":
    main()
