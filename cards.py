from client import Client

cl = Client() 

def get_cards(lid):
  return cl.get("/lists/" + lid + "/cards")

def create_card(lid, name, due):
  return cl.post("/cards", {'name': name, 'due': due, 'idList': lid, 'desc': "hi"})
  #cl.log_req(r, "card created", ['name', 'id'])

def close_card(cid):
  return cl.put("/cards/" + cid + "/closed", {'value': 'true'})
  #cl.log_req(r, "card closed", ['name', 'closed'])

def open_card(cid):
  return cl.put("/cards/" + cid + "/closed", {'value': 'false'})
  #cl.log_req(r, "card opened" + r.text)
