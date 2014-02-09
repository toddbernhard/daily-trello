#!/usr/bin/env python

from client import Client

app_key = ""
user_token = ""
with open("application_key", "r") as f:
  app_key = f.read().replace('\n','')
with open("token", "r") as f:
  user_token = f.read().replace('\n','')

my_bid = "fdfYIdoj"


cl = Client(app_key, user_token)

def get_lists(board_id):
  r = cl.get("/boards/" + board_id + "/lists")
  lists = r.json()
  return lists

def get_cards(list_id):
  r = cl.get("/lists/" + list_id + "/cards")
  cards = r.json()
  return cards

def get_list_id(list_name):
  mylists = get_lists(my_bid)
  filter(lambda x: x == list_name, mylists)
  
  if len(mylists) > 0:
    return mylists[0]['id']
  else:
    raise Exception("no list: " + list_name)

def read_list_from_file(list_name):
  import os
  curdir = os.path.dirname(__file__)
  filename = os.path.join(curdir, "lists/" + list_name)
  f = open(filename)

  items = f.readlines()
  return map(lambda x: x.rstrip(), items)

def add_card(lid, name, due):
  r = cl.post("/cards", {'name': name, 'due': due, 'idList': lid, 'desc': "hi"})
  print(r.status_code.__str__() + " card added: " + r.text)

def regen_list(list_name):
  lid = get_list_id(list_name)
  items = read_list_from_file(list_name)
  
  for item in items:
    add_card(lid, item, 'null')    

regen_list("Morning")

print("check cards")
for card in get_cards(get_list_id("Morning")):
  print(card)

#for item in read_list_from_file("Morning"):
#  print(item)

#print(get_list_id("Morning"))

#for tlist in lists:
#  print(tlist['name'])
#  print(get_cards(tlist['id']))
  
#detail = get_list(tlist['id'])
 # print(detail)
