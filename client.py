#!/usr/bin/env python

import requests

key = ""
token = ""
with open("application_key", "r") as f:
  key = f.read().replace('\n','')
with open("token", "r") as f:
  token = f.read().replace('\n','')


class Client:
  
  base_url = "https://api.trello.com/1"
  
  rest_map = {'get': requests.get, 'put': requests.put, 'post': requests.post}
  
  def __init__( self, application_key = key, user_token = token):
    self.auth = { 'key': application_key, 'token': user_token }
  
  def x( self, http_type, url, args = {} ):
    args.update(self.auth)
    fn = self.rest_map[http_type]
    return fn( self.base_url+url, params = args )

  def log_req( self, req, msg, keys = []):
    string = req.status_code.__str__() + " -- " + msg + " -- "
    for key in keys:
      string = string + key + ": " + req.json()[key] + ", "

    print(string)
  
  
  def get( self, url, args = {} ):
    return self.x( requests.get, url, args )

  def put( self, url, args = {} ):
    return self.x( requests.put, url, args )

  def update( self, url, args = {} ):
    return self.x( requests.update, url, args )

  def post( self, url, args = {} ):
    return self.x( requests.post, url, args )

  def delete( self, url, args = {} ):
    return self.x( requests.delete, url, args )

