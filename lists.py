from pprint import pprint
from client import Client

cl = Client()

def get_lists(bid):
  b = cl.get("/boards/" + bid + "/lists")
  #print("")
  #print("lists")
  #pprint(b)
  return b

def create_list(bid, name):
  print("new list ?!?! "+name)
  r = cl.post("/lists", { 'name': name, 'idBoard': bid } )
  print("create list call")
  pprint(r)

def get_list_id(bid, name):
  mylists = get_lists(bid)
  mylists = list(filter(lambda x: x['name'] == name, mylists))
  
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

