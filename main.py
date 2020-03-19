#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:48:09 2020

@author: bernardintheo
"""

import tweepy
import json
import time


#different token to make request thanks to tweepy
access_token = '1159875631670280201-OwZDsUeS6OLBhWQvgfrfSFYKT7zGTh'
access_token_secret = 'AvQvErKyVeWSqY2oQXzSgMFPvWcIHsfumgaVdJwOxmNWE'
consumer_key = 'ZAMVzUS5k26TOHfseycKXcmQc'
consumer_secret = 'Rk31yi8P4nuJVfUCpb6dp9zZ4XPGqcZ3fkdjpDF62oO8kUiot8'
    
#using our credential to instantiate a connection with tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
   

listeIdTweet = []
while True:
    for tweet in tweepy.Cursor(api.search, q=["corona","coronavirus","covid19"],until="2020-03-19", lang="fr", count=500).items():
        try:
            with open('data_corona1.txt','a') as tfs:
                if tweet._json['id'] not in listeIdTweet:
                    tfs.write(str(tweet._json['text']))
                    #separate the different JSON objects with a ,
                    tfs.write(" ")
                    listeIdTweet.append(tweet._json['id'])
            tfs.close()
            
            """
            with open('contenu_tweet.txt','a') as f:
                for mot in getContentTweet('data_corona.txt'):
                    f.write(mot)
            f.close()
            """
            
        except tweepy.TweepError:
            print("coucou")
            continue




    

 
  
