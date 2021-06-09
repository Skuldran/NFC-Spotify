# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:06:36 2021

@author: Axel
"""
import os
import json
import random

import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyInterface:
    
    def __init__(self):
        #Look for user data
        if os.path.isfile('userdata.json'):
            
            #Read user data from file
            with open('userdata.json', 'r') as fp:
                userdatadict = json.load(fp)
            
            client_id = userdatadict['SPOTIPY_CLIENT_ID']
            client_secret = userdatadict['SPOTIPY_CLIENT_SECRET']
            redirect_uri = userdatadict['SPOTIPY_REDIRECT_URI']

        else:
            #No user data found, let user enter it.
            client_id = input('Enter your client id: ');
            client_secret = input('Enter your client secret id: ')
            redirect_uri = input('Enter your redirect uri: ')
            
            userdatadict = {
                'SPOTIPY_CLIENT_ID': client_id,
                'SPOTIPY_CLIENT_SECRET': client_secret,
                'SPOTIPY_REDIRECT_URI': redirect_uri}
            
            with open('userdata.json', 'w') as fp:
                json.dump(userdatadict, fp)
            
        os.environ['SPOTIPY_CLIENT_ID'] = client_id
        os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
        os.environ['SPOTIPY_REDIRECT_URI'] = redirect_uri
        
        if os.path.isfile('data.json'):
            with open('data.json', 'r') as fp:
                self.states = json.load(fp)
        else:
            self.states = {}
            
        #Set up spotify communication
        scopes = 'user-read-currently-playing,user-read-playback-state,user-modify-playback-state'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))
    
    def reactToCard(self, nfc_id):
        if ~nfc_id in self.states:
            raise Exception('ID does not exist!')
        
        state = self.states[nfc_id];
        
        #Do stuff according to state.
        context = state['context']
        shuffle = state['shuffle']
        
        self.sp.shuffle(state=shuffle)
        self.sp.start_playback(context_uri=context)
        
    def saveCard(self):
        newID = random.randint(1, 10000);
        
        newID = 100;
        # Gather data from Spotipy playback
        # - Context
        # - Current track?
        # - Shuffle on/off
        
        curr_play = self.sp.current_playback()
        contDict = curr_play['context']
        context = contDict['uri']
        shuffle = curr_play['shuffle_state']
        
        #Create and save new state
        newState = {
            "id": newID,
            "context": context,
            "shuffle": shuffle}
        
        self.states[newID] = newState;
        
        with open('data.json', 'w') as fp:
            json.dump(self.states, fp)
        
        return newID
        
    def getSuitableDevice():
        print('')
        
        