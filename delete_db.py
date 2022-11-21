import csv

def delete_db():

    '''
    Функция удаления строки по фамилии ученика
    '''
    family = (input("Введите фамилию искомого ученика\n").title())# Первая буква автоматически заглавная
    with open("Pupils.csv","r", encoding='utf-8') as csvfile:
        newrows = []
        reader = csv.reader(csvfile) #открываем файл для чтения
        for row in reader:
            # записываем в список все строчки без family
            if family not in row:
                newrows.append(row)
            elif family in row:
                print(f"Ученик {family} удален из базы.")
                
    with open("Pupils.csv","w", encoding='utf-8', newline='',) as csvfile2:
            write=csv.writer(csvfile2, delimiter=',') # открываем файл для записи
            for line in newrows:
                write.writerow(line)
                

                
delete_db()