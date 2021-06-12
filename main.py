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
    
    if tagStatus["newTag"] == None:
        tagIsProgrammed = False
        continue
    
    #Change song if the tag is new
    if tagStatus["newTag"]:
        print("Playing spotify according to new tag.")
        tagIsProgrammed = False
        si.reactToCard(tagStatus["uid"])
        
    if tagStatus["tagAge"]>programTime & ~tagIsProgrammed:
        print("Attempt to program card.")
        si.saveCard(tagStatus["uid"])
        tagIsProgrammed = True
        print("Tag is programmed!")
        
