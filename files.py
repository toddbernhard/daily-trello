import yaml
import os
import re
from datetime import datetime
from pprint import pprint


def load_config():
  return yaml.load(open('config.yaml'))


def load_tasks_now():
  task_lists = dict()

  # get lists
  list_dir = os.path.join(os.path.dirname(__file__), "lists")
  for root,dirs,files in os.walk(list_dir):

    # load and filter tasks
    for filename in files:
      next_list = load_routine(os.path.join(root,filename))
      next_list['tasks'] = filter_now(next_list['tasks'])
      task_lists[next_list['name']] = next_list['tasks']
  
  return task_lists


def filter_now(tasks):

  # get now as time value
  now = datetime.now()
  if now.hour <= 6:
    now = 'morning'
  elif now.hour <= 12:
    now = 'noon'
  else:
    now = 'night'
  now = 'morning'

  tasks = list(filter(lambda x: (now in x['time']), tasks))

  def is_scheduled_daily(now, task):
    if task['schedule_option']['interval'] < 2:
      return True
    else:
      days = (now - datetime.utcfromtimestamp(0)).days
      if (days + task['schedule_option']['offset']) % (task['schedule_option']['interval']) == 0:
        return True
      else:
        return False

  def is_scheduled_weekly(now, task):
    weekdays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = weekdays[now.weekday()]
    return day in task['schedule_option']

  def is_scheduled(now, task):
    if task['schedule'] == 'daily':
      return is_scheduled_daily(now, task)
    elif task['schedule'] == 'weekly':
      return is_scheduled_weekly(now, task)

  tasks = list(filter(lambda x: is_scheduled(datetime.now(), x), tasks))

  return list(tasks)

#def save_day(lid):
#  name = get_list(lid)['name']
#  date_time = datetime.datetime.fromtimestamp(time.time.time()).strftime('%Y-%m-%d %H:%M:%S')
#  cards = get_cards(lid)


def validate_routine(routine):
  for task in routine:
    for key in ['name', 'keep_score', 'time', 'schedule', 'schedule_option']:
      assert(key in task)
    
    assert(isinstance(task['keep_score'], bool))

    at_morning = 'morning' in task['time']
    at_noon = 'noon' in task['time']
    at_night = 'night' in task['time']
    assert(at_morning or at_noon or at_night)

    assert(task['schedule'] in ['daily', 'weekly'])
    if task['schedule'] is 'daily':
      assert('interval' in task['schedule_option'] and 'offset' in task['schedule_option'])
    elif task['schedule'] is 'weekly':
      for days in task['schedule_option']:
        assert(days in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday'])


def load_routine(filename):
  routine = yaml.load(open(filename))

  # prepare defaults
  defaults = {'time': ['morning'],
              'schedule': 'daily',
              'schedule_option': {'interval': 1, 'offset': 0},
              'keep_score': True}

  if 'defaults' in routine:
    defaults.update(routine['defaults'])
    routine.pop('defaults')

  # fill out tasks with defaults
  for task in routine['tasks']:
    for k, v in defaults.items():
      if k not in task:
        task[k] = v

  validate_routine(routine['tasks'])
  return routine
