import csv
def Edit_rec():
    '''
    редактирует искомую запись в БД
    '''
    with open('Pupils.csv', 'r', newline='', encoding='utf-8') as pupils:
        r = csv.reader(pupils)
        lines = list(r)
    
    print("По какому параметру вы хотите найти ученика, информацию о котором хотите изменить?")
    for i in range (len(lines[0])):
        print(f'{i} - {lines[0][i]}')
    identificator_column = int(input('Введите соответсвущее число '))
    identificator = input(f'Введите искомое значение ')
    isFound = False
    for i in lines:
        if i[identificator_column] == identificator:
            isFound = True
            print("Значение какого параметра вы хотите изменить?")
            for j in range (len(lines[0])):
                print(f'{j} - {lines[0][j]}')
            changing_column = int(input('Введите соответсвущее число '))
            print(f'Текущее значение данного параметра {i[changing_column]}')
            new_value = input(f'Введите новое значение ')
            old_value = i[changing_column]
            i[changing_column] = new_value
            break

    #Записываем изменненый список в файл
    with open('Pupils.csv', 'w', newline='', encoding='utf-8') as pupils:
        writer = csv.writer(pupils, delimiter=',')
        writer.writerows(lines)

    if isFound :
        return print('Изменения весены.')
    else:
        return print("Запись не найдена")
# Edit_rec()
