import csv
def Create_db():
    with open('Pupils.csv', 'w', newline='', encoding='utf-8') as pupils:
        csv_writer = csv.writer(pupils, delimiter=',')
        csv_writer.writerow(['ID_Pupil', 'name', 'family name', 'class'])
        csv_writer.writerow(['001', 'Иван', 'Иванов', '1А'])
        csv_writer.writerow(['002', 'Семен', 'Семенов', '2А'])
        csv_writer.writerow(['003', 'Петр', 'Петров', '3А'])
    
    with open('Seats_status.csv', 'w', newline='', encoding='utf-8') as seats_status:
        csv_writer = csv.writer(seats_status, delimiter=',')
        csv_writer.writerow(['ID', 'BusyOrEmpty', 'StartTime', 'EndTime', 'ID_Seat', 'ID_Pupul'])
        csv_writer.writerow(['0001', 'Busy', '10:00 21.10.22', '11:00 21.10.22', '01','001' ])
        csv_writer.writerow(['0002', 'Busy', '10:00 21.10.22', '11:00 21.10.22', '02','002' ])
        csv_writer.writerow(['0003', 'Busy', '10:00 21.10.22', '11:00 21.10.22', '03','003' ])
    
    with open('Seats.csv', 'w', newline='', encoding='utf-8') as seats:
        csv_writer = csv.writer(seats, delimiter=',')
        csv_writer.writerow(['ID_Seat', 'Row', 'Line', 'LeftOrRight'])
        csv_writer.writerow(['01', '1', '1', 'Left'])
        csv_writer.writerow(['02', '1', '1', 'Right'])
        csv_writer.writerow(['03', '2', '1', 'Left'])
        csv_writer.writerow(['04', '2', '1', 'Right'])
        csv_writer.writerow(['05', '1', '2', 'Left'])
        csv_writer.writerow(['06', '1', '2', 'Right'])
        csv_writer.writerow(['05', '2', '2', 'Left'])
        csv_writer.writerow(['06', '2', '2', 'Right'])

Create_db()


    




