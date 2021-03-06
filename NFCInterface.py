# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:27:37 2021

@author: Axel
"""

import RPi.GPIO as GPIO

from pn532 import *
import time

class NFCInterface:
    
    #oldTag, oldTagArrival, askedForNewTag
    
    def __init__(self):
        try:
            self.pn532 = PN532_UART(debug=False, reset=20)
            
            self.pn532.SAM_configuration()
            
            
            self.oldTagArrival = time.perf_counter()
            self.oldTag = None
            print('PN532 is initialized')
        except Exception as e:
            print(e)
        
    def update(self):
        uid = self.pn532.read_passive_target(timeout=0.5)
        if uid is None:
            if self.oldTag != None:
                print('Lost the previous card.')
            self.oldTag = None
            return {"newTag": None,
                     "tagAge": None,
                     "uid": None}
        
        
        #uid = [hex(i) for i in uid]
        #uid = uid.decode('ascii')
        #uid = str(bytes(uid))
        #uid = long(uid)
        uid = str(int.from_bytes(uid, byteorder='big'))
        newTag = (uid != self.oldTag)
        if newTag:
            print('Found card with UID:', uid)
            self.oldTag = uid
            self.oldTagArrival = time.perf_counter()
            
        tagAge = time.perf_counter()-self.oldTagArrival

        print('The card has been here: ', tagAge)
        return {"newTag": newTag,
                "tagAge": tagAge,
                "uid": uid}
    
        
    def writeTag(self, data):
        print("Pranked")
