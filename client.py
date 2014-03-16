#!/usr/bin/env python

import requests
from files import load_config

config = load_config()

class Client:
  
  base_url = "https://api.trello.com/1"
  
  rest_map = {'get': requests.get, 'put': requests.put, 'post': requests.post}
  
  def __init__( self, application_key = config['application_key'], user_token = config['user_token']):
    self.auth = { 'key': application_key, 'token': user_token }
  
  def send( self, http_type, url, args = {} ):
    args.update(self.auth)
    # fn = self.rest_map[http_type]
    try:
      answer = http_type( self.base_url+url, params = args ).json()
      #print( str(answer) )
      return answer
    except:
      print("failed @ " + self.base_url+url + ", " + str(args))
      print( http_type( self.base_url+url, params = args ).text )

  def log_req( self, req, msg, keys = []):
    string = req.status_code.__str__() + " -- " + msg + " -- "
    for key in keys:
      string = string + key + ": " + req.json()[key] + ", "

    print(string)
  
  
  def get( self, url, args = {} ):
    return self.send( requests.get, url, args )

  def put( self, url, args = {} ):
    return self.send( requests.put, url, args )

  def update( self, url, args = {} ):
    return self.send( requests.update, url, args )

  def post( self, url, args = {} ):
    return self.send( requests.post, url, args )

  def delete( self, url, args = {} ):
    return self.send( requests.delete, url, args )

