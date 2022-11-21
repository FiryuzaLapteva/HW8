import csv
def Show_db(db_name):
    '''
    Красиво показывает все базы БД
    '''
    with open(db_name, encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reade = csv.reader(r_file, delimiter = ",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reade:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                # Вывод строк
                print(f'    {row[0]} - {row[1]} {row[2]} {row[3]} класс.')
            count += 1
        print(f'Всего в файле {count} строк(и).')

# Show_db('Pupils.csv')