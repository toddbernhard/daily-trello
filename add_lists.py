#!/usr/bin/env python

from client import Client
from lists import get_or_create_list as get_list
from pprint import pprint
from cards import get_cards, create_card, close_card, open_card

cl = Client()

my_bid = "fdfYIdoj"

def load_routine(list_name):
  import os
  curdir = os.path.dirname(__file__)
  filename = os.path.join(curdir, "lists/" + list_name)
  f = open(filename)

  items = f.readlines()
  return list(map(lambda x: {'name': x.rstrip()}, items))

def regen_list(list_name):
  def list_minus_list(list_a, list_b):
    c = []
    for a in list_a:
      exists = False

      for b in list_b:
        if a['name'] == b['name']:
          exists = True
          break

      if not exists:
        c.append(a)

    return c


  tasks = load_routine(list_name)
  #pprint(tasks)
    
  lid = get_list(my_bid, list_name)
  cards = get_cards(lid)
  #print(cards)

  new_tasks = list_minus_list(tasks, cards)
  old_cards = list_minus_list(cards, tasks)
  current_cards = list_minus_list(cards, old_cards)

  for task in new_tasks:
    create_card(lid, task['name'], 'null')
    #print("new task " + task['name'])

  for card in old_cards:
    close_card(card['id'])
    #print("old cards " + card['name'])

  for card in current_cards:
    #print("current card " + card['name'])
    if card['closed']:
      open_card(card['id'])

regen_list("Morning")

print("check cards")
for card in get_cards(get_list(my_bid, "Morning")):
  print("# " + card['name'] + " :: " + card['id'])
