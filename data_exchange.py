import json
import datetime

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")

#serial
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
        f.close()
  except:
      pass#cpuserial = "ERROR000000000"
 
  return cpuserial

#str to json
def msg(user:str, password:int, pass_type:str):
    serial = getserial()
    data = {'user_info':user,
            'address': "rua 1",
            'password_type': pass_type,
            'password':password,
            'time': current_time,
            'serial': serial
            }
    data = json.dumps(str(data))
    #new_string = json.dumps(data)
    print(data)