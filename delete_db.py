import csv

def Delete_db():

    '''
    Функция удаления строки по фамилии ученика
    '''
    family = (input("Введите фамилию искомого ученика\n").title())# Первая буква автоматически заглавная
    with open("Pupils.csv","r", encoding='utf-8') as csvfile:
        newrows = []
        is_student_in_db = False #маркер, проверяющий, если ли искомый ученик в базе данных
        reader = csv.reader(csvfile) #открываем файл для чтения
        for row in reader:
            # записываем в список все строчки без family
            if family not in row:
                newrows.append(row)
            else:
                is_student_in_db = True
                
                
    with open("Pupils.csv","w", encoding='utf-8', newline='',) as csvfile2:
            write=csv.writer(csvfile2, delimiter=',') # открываем файл для записи
            for line in newrows:
                write.writerow(line)

    if is_student_in_db:
        print(f"Ученик {family} удален из базы.")
    else:
        print(f"Ученик {family} не был найден в базе.")
                
# Delete_db()