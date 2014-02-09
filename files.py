from client import Client
from lists import get_list
from cards import get_cards

cl = Client()

def save_day(lid):
  name = get_list(lid)['name']
  date_time = datetime.datetime.fromtimestamp(time.time.time()).strftime('%Y-%m-%d %H:%M:%S')
  cards = get_cards(lid)
