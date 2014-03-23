from client import Client

cl = Client() 

def get_cards(lid):
  return cl.get("/lists/" + lid + "/cards").json

def create_card(lid, name, due):
  return cl.post("/cards", {'name': name, 'due': due, 'idList': lid, 'desc': "hi"}).json
  #cl.log_req(r, "card created", ['name', 'id'])

def close_card(cid):
  return cl.put("/cards/" + cid + "/closed", {'value': 'true'}).json
  #cl.log_req(r, "card closed", ['name', 'closed'])

def open_card(cid):
  return cl.put("/cards/" + cid + "/closed", {'value': 'false'}).json
  #cl.log_req(r, "card opened" + r.text)

def get_card_id(lid, name):
  cards = get_cards(lid)
  cards = list(filter(lambda x: x['name'] == name, cards))
  
  if len(cards) > 0:
    print("--   pos: " + str(cards[0]['pos']))
    return cards[0]['id']
  else:
    raise Exception("no card: " + name)

def get_or_create_card(lid, name):
  try:
    cid = get_card_id(lid, name)
  except Exception:
    create_card(lid, name, 'null')
    cid = get_card_id(lid, name)

  return cid

