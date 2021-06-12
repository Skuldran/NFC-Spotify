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
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyInterface:
    
    currently_playing = None
    
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
            
            print(self.states)
        else:
            self.states = {}
            
        #Set up spotify communication
        scopes = 'user-read-currently-playing,user-read-playback-state,user-modify-playback-state'
        
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))
    
    def reactToCard(self, nfc_id):
        if not nfc_id in self.states:
            print("ID haas not been saved: ", nfc_id);
            return
        
        state = self.states[nfc_id];
        
        #Do stuff according to state.
        context = state['context']
        shuffle = state['shuffle']
        
        if self.currently_playing == context:
            print("Already playing this state.")
        
        self.currently_playing = context
        self.sp.shuffle(state=shuffle)
        self.sp.start_playback(context_uri=context)
        
    def saveCard(self, ID):
        # Gather data from Spotipy playback
        # - Context
        # - Current track?
        # - Shuffle on/off
        
        curr_play = self.sp.current_playback()
        contDict = curr_play['context']
        context = contDict['uri']
        shuffle = curr_play['shuffle_state']
        print("Got whats currently playing.")        
        #Create and save new state
        newState = {
            "id": ID,
            "context": context,
            "shuffle": shuffle}
        
        self.states[ID] = newState;
        
        with open('data.json', 'w') as fp:
            json.dump(self.states, fp)
        print("Saved to json: ", ID)
        print(self.states)
        
    def getSuitableDevice():
        print('')
        
        
