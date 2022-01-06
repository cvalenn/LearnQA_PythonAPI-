import requests
import json


#Задание 1

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response1.text)
print(response1.status_code)

#Задание 2

response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response2.text)
print(response2.status_code)

#Задание 3

response3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
print(response3.text)
print(response3.status_code)

#Задание 4

methods = [{"method":"GET"}, {"method":"PUT"}, {"method":"DELETE"}, {"method":"POST"}]

for i in methods:
    response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    try:
        if "success" in json.loads(response_post.text):
            print("POST запрос успешен с методом", i)     
    except:
        pass  
    response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    try:
        if "success" in json.loads(response_put.text):
                print("PUT запрос успешен с методом", i)     
    except:
        pass  
    response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i)
    try:
        if "success" in json.loads(response_get.text):
            print("GET запрос успешен с методом", i)     
    except:
        pass       
    response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    try:
        if "success" in json.loads(response_delete.text):
            print("DELETE запрос успешен с методом", i)     
    except:
        pass   
