#Ex8:

import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print('1. ' + str(response.status_code) + ' ' + response.text)
parsed_task0 = response.json()
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":parsed_task0['token']})
task0_status = response.json()
st0 = 'status'
if task0_status[st0] == 'Job is NOT ready':
    print('2. ' + str(response.status_code) + ' ' + response.text)
else:
    print('2. WARNING: Unexpected task status')
print('3. Waiting timeout...')
time.sleep(parsed_task0['seconds'])
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":parsed_task0['token']})
parsed_task1 = response.json()
res, st1 = 'result', 'status'
if parsed_task1[st1] == 'Job is ready':
    if parsed_task1[res] is not None:
        print('4. ' + str(response.status_code) + ' ' + response.text)
    else:
        print('4. WARNING: Result is not avaible')
else:
    print('4. WARNING: Unexpected task status')
