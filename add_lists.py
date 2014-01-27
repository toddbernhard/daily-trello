#!/usr/bin/env python

from client import Client

app_key = ""
user_token = ""
url_base = "https://api.trello.com/1"

with open("application_key", "r") as f:
  app_key = f.read().replace('\n','')

with open("token", "r") as f:
  user_token = f.read().replace('\n','')

print("key="+app_key+" token="+user_token)

cl = Client(app_key, user_token)

r = cl.get("/boards/fdfYIdoj")

print(r.url)
print(r.status_code)
print(r.text)
