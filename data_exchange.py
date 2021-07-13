import json
import datetime
import os
from twilio.rest import Client

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

#send sms
def send_sms():
    try:
        print (os.getenv('ACCOUNT_SID'))
        print (os.getenv('AUTH_TOKEN'))        
        account_sid = os.environ['ACCOUNT_SID']
        auth_token = os.environ['AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        
        message = Client.messages.create(
                         from_='',
                         to='',
                         body="test"
                     )
    except:
         print(message.sid)

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
    send_sms()
