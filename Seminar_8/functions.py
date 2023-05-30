import shutil


def show_menu():
    print("\nВыберите нужное действие: \n"
          "1.Отобразить весь справочник\n"
          "2.Найти абонента по имени\n"
          "3.Найти абонента по фамилии\n"
          "4.Найти абонента по номеру\n"
          "5.Добавить абонента\n"
          "6.Удалить абонента\n"
          "7.Изменить данные абонента\n"
          "8.Сохранить справочник в текстовом формате\n"
          "9.Закончить работу\n")
    choice = int(input())
    return choice


def parse_csv(filename: str):
    """Трансформируем справочник в список словарей"""
    results = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            record = dict(zip(fields, line.strip().split(',')))
            results.append(record)
    return results


def work_with_phonebook():
    """Функции работы с телефонной книгой в зависимости от меню"""
    choice = show_menu()
    phone_book = parse_csv('Seminar_8\\phonebook.csv')
    while (choice != 9):
        if choice == 1:
            show_phonebook(phone_book)
        elif choice == 2:
            show_phonebook(find_by_name(phone_book))
        elif choice == 3:
            show_phonebook(find_by_surname(phone_book))
        elif choice == 4:
            show_phonebook(find_by_number(phone_book))
        elif choice == 5:
            add_new_user(phone_book)
            write_csv('Seminar_8\\phonebook.csv', phone_book)
        elif choice == 6:
            delete_user(phone_book)
            rewrite_csv('Seminar_8\\phonebook.csv', phone_book)
        elif choice == 7:
            change_userdata(phone_book)
            rewrite_csv('Seminar_8\\phonebook.csv', phone_book)
        elif choice == 8:
            make_txt()    
        choice = show_menu()


def show_phonebook(phone_book):
    """1. Отображение справочника"""
    for elem in phone_book:
        for key in elem:
            print(f"{key} : {elem[key]}")
        print('-'*10)


def find_by_name(phone_book):
    """2. Поиск абонента по имени"""
    name = input("Введите имя для поиска: ")
    results = []
    for elem in phone_book:
        if elem['Имя'].lower() == name.lower():
            results.append(elem)
    return results                


def find_by_surname(phone_book):
    """3. Поиск абонента по фамилии"""
    surname = input("Введите фамилию для поиска: ")
    results = []
    for elem in phone_book:
        if elem['Фамилия'].lower()  == surname.lower():
            results.append(elem)
    return results 


def find_by_number(phone_book):
    """4. Поиск абонента по номеру"""
    number = input("Введите номер для поиска: ")
    results = []
    for elem in phone_book:
        if elem['Телефон'] == number:
            results.append(elem)
    return results 


def add_new_user(phone_book):
    """5. Добавить нового абонента"""
    record = dict()
    for k in phone_book[0].keys():
        record[k] = input(f'Введите {k}: ')
    phone_book.append(record)    


def write_csv(filename: str, phone_book: list):
    with open(filename, 'a', encoding='utf-8') as data:
        line = ''
        for v in phone_book[-1].values():
            line += v + ','
            data.write(f'{line[:-1]}\n')


def delete_user(phone_book):
    """6. Удалить абонента"""
    user = input('Введите фимилию абонента, которого желаетет удалить: ') 
    for elem in phone_book:
        for v in elem.values():
            if v.lower() == user.lower():
                phone_book.remove(elem)


def rewrite_csv(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as data:
        for i in range(len(phone_book)):
            line = ''
            for v in phone_book[i].values():
                line += v + ','
            data.write(f'{line[:-1]}\n')  


def change_userdata(phone_book):
    """7. Изменить данные абонента"""
    user = input('Введите фамилию абонента, данные которого желаете изменить: ')
    changed_atr = input('Введите атрибут, который желаете изменить: ')
    new_atr = input('Введите новое значение атрибута: ')
    for elem in phone_book:
        for v in elem.values():
            if v == user:
                elem[changed_atr] = elem[changed_atr].replace(elem[changed_atr], new_atr)


def make_txt():
    """8. Сохранить справочник в тектовом формате"""
    filename = input('Введите имя для сохранения: ')
    shutil.copyfile('Seminar_8\\phonebook.csv', f'{filename}.txt')


work_with_phonebook()
