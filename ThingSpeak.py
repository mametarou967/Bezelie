#! /usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import json
import time

class ThingSpeak :
  def __init__(self,API_KEY,ID,MaxDistance,MinDistance) :
    self.API_KEY = API_KEY
    self.ID = ID
    self.MaxDistance = int(MaxDistance)
    self.MinDistance = int(MinDistance)
    print("start")
    
  def existTrashBox(self) :
    url = "http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" % (self.ID,self.API_KEY)
    TS = urllib.request.urlopen(url=url)
    response = TS.read()
    data=json.loads(response.decode())
    b = data['field1']
    print(b)
    distance  = float(data['field1'])
    if self.MaxDistance > distance : 
      print(distance)
      return True
    else :
      print(distance)
      return False

