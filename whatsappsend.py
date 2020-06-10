import pyautogui as pg, time
import subprocess
import json
message = '''
Hello {}, 
How are you?
How is {} doing?
I hope {} is doing well & taking good care of you
Bye
{}
'''


cmd = "/Users/kush/PycharmProjects/Spamming/scratch.sh {}"
# returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

def send_message(m):
    for x in m:
        pg.typewrite(x)
        pg.hotkey('shift','enter')
    pg.press('enter')

with open('data.json') as f:
  names_data = json.load(f)

for x in names_data:
    recipient_name = x.get('name')
    kid = x.get('kid')
    spouse = x.get('spouse')
    phone = x.get('phone')
    print(message.format(recipient_name,kid,spouse, 'Kush'))
    returned_value = subprocess.call(cmd.format(phone), shell=True)
    print('returned value:', returned_value)
    time.sleep(1)
    msg = message.format(recipient_name,kid,spouse, 'Kush')
    msg_list = msg.split('\n')
    send_message(msg_list)




# phone = '14082037236'
# message = 'hello from automated kush'

# time.sleep(1)
# send_message(message)
