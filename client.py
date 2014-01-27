#!/usr/bin/env python

import requests

app_key = ""
user_token = ""
url_base = "https://api.trello.com/1"

with open("application_key", "r") as f:
  app_key = f.read().replace('\n','')

with open("token", "r") as f:
  user_token = f.read().replace('\n','')

print("key="+app_key+" token="+user_token)

auth = {'key': app_key, 'token': user_token}
r = requests.get("https://api.trello.com/1/boards/fdfYIdoj", params = auth)


print(r.url)
print(r.status_code)
print(r.text)

new_card = {}
print(new_card)
new_card.update(auth)
print(new_card)
r = requests.post(url_base + "/cards", params = new_card)


print(r.url)
print(r.status_code)
print(r.text)
