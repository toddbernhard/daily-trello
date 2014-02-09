
from client import Client

cl = Client()

def get_lists(bid):
  r = cl.x('get', "/boards/" + bid + "/lists")
  lists = r.json()
  return lists

def create_list(bid, name):
  r = cl.x('post', "/lists", { 'name': name, 'idBoard': bid } )
  print(r.status_code.__str__() + " list created: " + r.text)

def get_list_id(bid, name):
  mylists = get_lists(bid)
  filter(lambda x: x == name, mylists)
  
  if len(mylists) > 0:
    return mylists[0]['id']
  else:
    raise Exception("no list: " + name)

def get_or_create_list(bid, name):
  try:
    lid = get_list_id(bid, name)
  except Exception:
    create_list(bid, name)
    lid = get_list_id(bid, name)

  return lid

