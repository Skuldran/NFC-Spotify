# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:27:37 2021

@author: Axel
"""

import RPi.GPIO as GPIO

from pn532 import *
import time

class NFCInterface:
    
    oldTag, oldTagArrival, askedForNewTag
    
    def __init__(self):
        try:
            pn532 = PN532_UART(debug=False, reset=20)
            
            pn532.SAM_configuration()
            
            
            self.oldTagArrival = time.perf_counter()
            self.oldTag = None
            print('PN532 is initialized')
        except Exception as e:
            print(e)
        finally:
            GPIO.cleanup()
        
    def update(self):
        uid = pn532.read_passive_target(timeout=0.5)
        if uid is None:
            return {"newTag": None,
                     "tagAge": None,
                     "uid": None}
        
        print('Found card with UID:', [hex(i) for i in uid])
        
        newTAg= (uid != self.oldTag)
        if newTag:
            self.oldTag = uid
            self.oldTagArrival = time.perf_counter()
            
        
        return {"newTag": newTag,
                "tagAge": self.oldTAgArrival - time.perf_counter(),
                "uid": uid}
    
        
    def writeTag(self, data):
        print("Pranked")