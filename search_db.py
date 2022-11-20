import csv

def Search_pupil(pupil_lastName):
    with open('Pupils.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        isFinded = False
        for row in csv_reader:
            # print(row[2])
            if row[2] == pupil_lastName:
                return row
                isFinded = True
                break
        if isFinded == False:
            return print ("Ученик с такой фамилией не найден")
        
print(Search_pupil("Иванов"))

