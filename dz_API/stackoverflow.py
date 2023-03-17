import requests
import datetime

url = 'https://api.stackexchange.com/2.3/questions?page=1&pagesize=10&fromdate={}&order=desc&sort=activity&tagged=python&site=stackoverflow'
# Для изменения кол-ва выводов изменить pagesize
two_days_ago = datetime.datetime.now() - datetime.timedelta(days=2)
from_date = int(two_days_ago.timestamp())
response = requests.get(url.format(from_date))

items = response.json()['items']
print("Вывод вопросов: ")
for item in items:
    print(item['title'])
