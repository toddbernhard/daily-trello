#!/usr/bin/env python

import requests


class Client:
    
    base_url = "https://api.trello.com/1"

    def __init__( self, application_key, user_token ):
        self.auth = { 'key': application_key, 'token': user_token }

    def get( self, url, args = {} ):
        args.update(self.auth)        
        return requests.get( self.base_url+url, params = args )

    def put( self, url, args = {} ):
        args.update(self.auth)        
        return requests.put( self.base_url+url, params = args )

    def update( self, url, args = {} ):
        args.update(self.auth)        
        return requests.update( self.base_url+url, params = args )

    def post( self, url, args = {} ):
        args.update(self.auth)        
        return requests.post( self.base_url+url, params = args )

