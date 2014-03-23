import yaml
import os
import re
from datetime import datetime
from pprint import pprint


def load_config():
  config_file = os.path.join(os.path.dirname(__file__), "config.yaml")
  return yaml.load(open(config_file))


def get_list_files():
  exclude_example = load_config()['turn_off_example']

  list_dir = os.path.join(os.path.dirname(__file__), "lists")
  for root,dirs,files in os.walk(list_dir):

    if exclude_example:
      files = filter(lambda x: x != 'example.yaml', files)

    return list(map(lambda x: os.path.join(root,x), files))

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
