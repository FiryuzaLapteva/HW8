from view import Get_action, Get_surname
from show_db import Show_db
from delete_db import Delete_db
from add_db import Add_db
from search_db import Search_pupil
from edit_record import Edit_rec
from logger import sclool_logger
import sys

def LaunchProject():
    while True:

        action = Get_action()
        print(action)

        if action == 6:
            sclool_logger(action)
            sys.exit("Вы завершили работу с базой данных")
        if action == 1:
            Show_db('Pupils.csv')
        elif action == 2:
            Search_pupil(Get_surname())
        elif action == 3:
            Delete_db()
        elif action == 4:
            Add_db('Pupils.csv')
        elif action == 5:
            Edit_rec()

        sclool_logger(action)