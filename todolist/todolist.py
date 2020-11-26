"""
1. 취소선 그리기
2. 질문 되묻기
31. 취소선 그리기1. 취소선 그리기1. 취소선 기기기기기기기기기그리. 오늘꺼 찾기
"""

import os.path
import json
import datetime
now = datetime.datetime.now()

def init():
    year = now.strftime("%Y-%y")
    month = now.strftime("%M-%m")
    day = now.strftime("%D-%d")
    date = now.strftime("%y%m%d")


    #number = int(input("숫자를 입력하세요: "))
    #if number == 13:
    #    print("correct!")
    #else:
    #    print("incorrent T_T")
    
    try:
        #today_msg = globals()['todolist'+today]()
        msg = load_data(date)

    except:
        #파일 생성하고
        #똑같이
        msg = "오늘은 ToDoList가 없어요"
   
    print(msg)
 
    menu = int(input("1)추가 2)완료\n")) 
    
    if menu == 1:
        input_todo = input("할 일을 입력하세요!\n")

        add_todo(date, input_todo)


    elif menu == 2:
        print("완료!")

def add_todo(date, todo):
    file_nm = "todolist{}.json".format(date)

    with open(file_nm) as f:
        json_data = json.load(f)


    with open(file_nm, "w") as f:
        json_data.append({
            "id": 13,
            "date": date,
            "todo": todo,
            "is_done": False 
            })
        json.dump(json_data, f)
        f.close()
        init()
    
def load_data(date):
    print("load_data")
    file_nm = "todolist{}.json".format(date)
    print(file_nm)
    if os.path.isfile(file_nm) == False:
        f = open(file_nm, "a")
        f.write("[\n]")
        f.close()

    print("here__")
    
    with open(file_nm) as f:
        print("opened")
        todo_json = json.load(f)
        print(todo_json)

    print(todo_json)

    msg = "오늘의 할 일!\n"
    todolist = []
    for todo in todo_json:
        if todo['is_done'] == True:
            todolist.append("[v] {}\n".format(todo['todo']))
        else:
            todolist.insert(0, "[ ] {}\n".format(todo['todo']))
        
    for todo in todolist:
        msg = msg + todo

    return msg 

def todolist201126():
    return load_data()

def todolist201125():
    
    #json_file = open("todolist.json", "r")
    #json_data = json.load(json_file)
    #json_data['testObject2'] = {'obj1': 1}

    with open("todolist.json") as f:
        json_data = json.load(f)
        print(json_data)
    
    #with open("todolist.json", "w") as f:
    #    json_data['obj3'] = 3
    #    json.dump(json_data, f)

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
