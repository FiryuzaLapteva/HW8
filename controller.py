from view import Get_action, Get_surname
from show_db import Show_db
# from delete_db import delete_db
# from add_db import add_db
from search_db import Search_pupil

def LaunchProject():
    action = Get_action()
    if action == 1:
        Show_db('Pupils.csv')
    elif action == 2:
        Search_pupil(Get_surname())
    # elif action == 3:
    #     delete_db()
    # elif action == 4:
    #     add_db.add_db()
    # elif action == 5:
    #     print('do5')