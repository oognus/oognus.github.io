"""
1. 취소선 그리기
2. 질문 되묻기
31. 취소선 그리기1. 취소선 그리기1. 취소선 기기기기기기기기기그리. 오늘꺼 찾기
"""

import json
import datetime
now = datetime.datetime.now()

def init():
    year = now.strftime("%Y-%y")
    month = now.strftime("%M-%m")
    day = now.strftime("%D-%d")
    today = now.strftime("%y%m%d")

    today_msg = globals()['todolist'+today]()

def todolist201125():
    
    #json_file = open("todolist.json", "r")
    #json_data = json.load(json_file)
    #json_data['testObject2'] = {'obj1': 1}

    with open("todolist.json") as f:
        json_data = json.load(f)
    
    with open("todolist.json", "w") as f:
        json_data['obj3'] = 3
        json.dump(json_data, f)

    #print(json_data)


    #json_file.close()
    



    #with open('todolist.json') as f:
    #    data = json.load(f)

    #print(data['testObject'])
    todolist = """

    """


    return todolist 

def test():
    msg = """
[v] todolist1
[v] todolist2
[ ] todolist3
    """
    print(msg)

#
init()
