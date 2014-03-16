import yaml
import os
from datetime import datetime
from enum import Enum

time = Enum('time', 'morning noon night')

def load_config():  
  return yaml.load(open('config.yaml'))

def load_tasks_now():
  
  # get now as time value
  now = datetime.now()
  if now.hour <= 6:
    now = time.morning
  else if now.hour <= 12:
    now = time.noon
  else:
    now = time.night

  # get lists
  list_dir = os.path.join(os.path.dirname(__file__), "lists")
  _,dirs,lists = os.walk(list_dir)
  
  # load and filter tasks
  task_lists = dict()
  for filename in lists:
    task_listsdididload_routine(filename)

#def save_day(lid):
#  name = get_list(lid)['name']
#  date_time = datetime.datetime.fromtimestamp(time.time.time()).strftime('%Y-%m-%d %H:%M:%S')
#  cards = get_cards(lid)

def load_routine(filename):
  print(filename)
  routine = yaml.load(open(filename))

  items = f.readlines()
  return list(map(lambda x: {'name': x.rstrip()}, items))
