import requests
import json
import time


#Ставим задачу
resp = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
id_task = (json.loads(resp.text))["token"]
seconds = json.loads(resp.text)["seconds"]

# Запрос до готовности задачи
resp_before_task_completed = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":id_task})
status = json.loads(resp_before_task_completed.text)["status"]
assert status == "Job is NOT ready"
time.sleep(seconds)

# Запрос после того как задача готова
resp_after_task_completed = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":id_task})
status_after = json.loads(resp_after_task_completed.text)["status"]
result = json.loads(resp_after_task_completed.text)["result"]
assert status_after == "Job is ready" and result is not None
print(status_after, ", result = ", result)


