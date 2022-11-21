import csv
def add_db (csvFileName):
    '''
    Функция добавляющая новые данные по ученику в строчку
    '''
    elementsToAppend ={'ID_Pupil':"5",
                        'name':"Ирина",
                        "family name":"Сенцова",
                        "class": "2д"}
    elementsToAppend['ID_Pupil'] = input ('Введите ID ')
    elementsToAppend['name'] = input ('Введите имя ')
    elementsToAppend['family name'] = input ('Введите фамилию ')
    elementsToAppend['class'] = input ('Введите класс ')
    with open(csvFileName, 'a+', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID_Pupil', 'name', 'family name', 'class']
        append_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        append_writer.writerow(elementsToAppend)
    print('\nИзменения внесены\n') 


add_db('Pupils.csv')
 
