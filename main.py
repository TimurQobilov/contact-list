contacts = []

def display_contacts():
    if not contacts:
        print("Список контактов пуст.")
    else:
        print("Ваши контакты:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Имя: {contact['name']}, Телефон: {contact['phone']}")

def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    contacts.append({"name": name, "phone": phone})
    print(f"Контакт {name} добавлен.")

def delete_contact():
    display_contacts()
    if contacts:
        try:
            index = int(input("Введите номер контакта для удаления: ")) - 1
            if 0 <= index < len(contacts):
                deleted_contact = contacts.pop(index)
                print(f"Контакт {deleted_contact['name']} удален.")
            else:
                print("Контакт с таким номером не существует.")
        except ValueError:
            print("Пожалуйста, введите корректный номер.")

def edit_contact():
    display_contacts()
    if contacts:
        try:
            index = int(input("Введите номер контакта для редактирования: ")) - 1
            if 0 <= index < len(contacts):
                new_name = input("Введите новое имя: ")
                new_phone = input("Введите новый номер телефона: ")
                contacts[index]['name'] = new_name
                contacts[index]['phone'] = new_phone
                print(f"Контакт {new_name} обновлен.")
            else:
                print("Контакт с таким номером не существует.")
        except ValueError:
            print("Пожалуйста, введите корректный номер.")

def menu():
    while True:
        print("\n=== Меню ===")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Изменить контакт")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            display_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")

if __name__ == '__main__':
    menu()
