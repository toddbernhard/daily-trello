from pprint import pprint
from client import Client

cl = Client()

def get_boards(username):
  print("available boards:")
  r = cl.get("/members/" + username + "/boards").json
  pprint(list(map(lambda x: {'name': x[u'name'], 'id': x[u'id']},r)))
  return r

def create_board(usernam, name):
  print("new list ?!?! "+name)
  r = cl.post("/lists", { 'name': name, 'idBoard': bid } )
  print("create list call")
  pprint(r)

def get_board_id(username, name):
  boards = get_boards(username)
  boards = list(filter(lambda x: x['name'] == name, boards))
  
  if len(boards) > 0:
    return boards[0]['id']
  else:
    raise Exception("no board: " + name)

def get_or_create_board(username, name):
  #try:
  lid = get_board_id(username, name)
  #except Exception:
  #create_list(bid, name)
  #lid = get_board_id(username, name)

  return lid

