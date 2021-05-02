import json
import datetime

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
#python to json
def msg(user:str, password:int):
    data = {'user_info':user,
            'end': "rua 1",
            'password':password,
            'time': current_time,
            }
    data = '"' + str(data) + '"'
    data = json.loads(str(data))
    new_string = json.dumps(data)
    print(new_string)
    

    