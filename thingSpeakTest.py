#! /usr/bin/python3
# -*- coding: utf-8 -*-

from ThingSpeak import ThingSpeak

thingSpeak = ThingSpeak("35ERMNSWBAQFSFYG","844648",300,5)
if thingSpeak.existTrashBox() :
  print("ものがあります")
else :
  print("ものがありません")
