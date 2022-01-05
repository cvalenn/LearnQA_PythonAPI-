import requests
import json
import time

#cтавим задачу
resp = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(resp.url)
print(resp.text)
token = (json.loads(resp.text))["token"]
seconds = json.loads(resp.text)["seconds"]

#запрос до готовности задачи
resp_before_task_completed = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(resp_before_task_completed.url)
print(resp_before_task_completed.text)
time.sleep(seconds)

#запрос после готовности задачи
resp_after_task_completed = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(resp_before_task_completed.url)
print(resp_after_task_completed.text)

