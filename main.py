# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:42:55 2021

@author: Axel
"""

import SpotifyInterface
import NFCInterface
import ArduinoInterface

si = SpotifyInterface.SpotifyInterface();
nfc = NFCInterface.NFCInterface();
ai = ArduinoInterface();

tagIsProgrammed = False
programmingState = False;

ai.setColor('green')

while(True):
    if ai.buttonPressed():
        programmingState = ~programmingState
        if programmingState:
            ai.setColor('yellow')
            tagIsProgrammed = False
        else:
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
            ai.setColor('green')
        else:
            print("Playing spotify according to new tag.")
            ai.setColor('blue')
            si.reactToCard(tagStatus["uid"])
            ai.setColor('green')
        
