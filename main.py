# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:42:55 2021

@author: Axel
"""

import SpotifyInterface
import NFCInterface

programTime = 5;

si = SpotifyInterface.SpotifyInterface();
nfc = NFCInterface.NFCInterface();

tagIsProgrammed = False

while(True):
    tagStatus = nfc.update();
    
    #No tag is currently in place
    if tagStatus["newTag"] == None:
        tagIsProgrammed = False
        continue
    
    #Change song if the tag is new
    if tagStatus["newTag"]:
        print("Playing spotify according to new tag.")
        si.reactToCard(tagStatus["uid"])
        
    if tagStatus["tagAge"]>programTime and ~tagIsProgrammed:
        si.saveCard(tagStatus["uid"])
        tagIsProgrammed = True
        print("Tag is programmed!")
        
