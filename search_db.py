import csv

def Search_pupil(pupil_lastName):
    with open('Pupils.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        isFinded = False
        for row in csv_reader:
            # print(row[2])
            if row[2] == pupil_lastName:
                return print(f' {row[0]} - {row[1]} {row[2]} {row[3]} класс.')
                isFinded = True
                break
        if isFinded == False:
            return print ("Ученик с такой фамилией не найден")              
# Search_pupil("Иванов")

# def Search_index_of_pupil_record():
#     '''
#    функция поиска индекса записи в бд по фамилии - такое себе для csv
#     '''
#     with open('Pupils.csv', 'r', encoding='utf-8') as csvfile:
#         csv_reader = csv.reader(csvfile, delimiter=',')
#         row_count = sum(1 for row in csv_reader)
#         # print(row_count)     
#     for i in range (row_count):
#         print(csv_reader[i])
# Search_index_of_pupil_record()