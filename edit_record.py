import csv
def Edit_rec(db_name, surname):
    '''
    редактирует искомую запись в БД
    '''
    r = csv.reader(open(db_name,"r", encoding='utf-8')) # Here your csv file
    lines = list(r)
    print(lines)
    
    


# Edit_rec("Pupils.csv", 'Иванов')
