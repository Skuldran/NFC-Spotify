# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:42:55 2021

@author: Axel
"""

import SpotifyInterface
import NFCInterface
import ArduinoInterface
import time

si = SpotifyInterface.SpotifyInterface();
nfc = NFCInterface.NFCInterface();
ai = ArduinoInterface.ArduinoInterface();

tagIsProgrammed = False
programmingState = False;

ai.setColor('green')

time.sleep(0.1)
while(True):
    if ai.buttonPressed():
        programmingState = ~programmingState
        if programmingState:
            print("Device set to programming state.")
            ai.setColor('yellow')
            tagIsProgrammed = False
        else:
            print("Device set to play state.")
            ai.setColor('green')
    
    tagStatus = nfc.update();
    
    #No tag is currently in place
    if tagStatus["newTag"] == None:
        tagIsProgrammed = False
        continue
    
    #Change song if the tag is new
    if tagStatus["newTag"]:
        if programmingState and ~tagIsProgrammed:
            print("Programming tag.")
            ai.setColor('blue')
            si.saveCard(tagStatus["uid"])
            tagIsProgrammed = True
            programmingState = False
            ai.setColor('green')
        else:
            print("Playing spotify according to new tag.")
            ai.setColor('blue')
            si.reactToCard(tagStatus["uid"])
            ai.setColor('green')
        
