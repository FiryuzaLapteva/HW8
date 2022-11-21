from datetime import datetime as dt
from view import Get_action

def sclool_logger(mode):
    '''
    Функция записывает в файл номер операции
    и время исполения
    '''
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write('операция {} выполнена в {};\n'
                    .format(mode, time))