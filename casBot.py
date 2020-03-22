#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:34:33 2020

@author: bernardintheo
"""

from covid import Covid
import tweepy
import datetime
from main import ecritureXLSX

#different token to make request thanks to tweepy

access_token = 'your token here'
access_token_secret = 'your token here'
consumer_key = 'your token here'
consumer_secret = 'your token here'
    
#using our credential to instantiate a connection with tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)



covid = Covid()

confirmedFrance = covid.get_status_by_country_name("france")['confirmed']

deathsFrance = covid.get_status_by_country_name("france")['deaths']
recoveredFrance = covid.get_status_by_country_name("france")['recovered']

totalConfirmed = covid.get_total_confirmed_cases()
totalRecovered = covid.get_total_recovered()
totalDeaths = covid.get_total_deaths()

percConfFr = round((confirmedFrance/totalConfirmed)*100,2)
percDeathsFr = round((deathsFrance/totalDeaths)*100,2)
percRecovFr = round((recoveredFrance/totalRecovered)*100,2)

temps = datetime.datetime.now()


ec = ecritureXLSX()

ec.ecrireXLSX('data/donneesCorona.xlsx','France',[[temps,confirmedFrance,deathsFrance,recoveredFrance]])
ec.ecrireXLSX('data/donneesCorona.xlsx','Monde',[[temps,totalConfirmed,totalDeaths,totalRecovered]])


lastIdStatus = api.user_timeline(screen_name = '6ita6chi6', count = 1)[0]

api.update_status("Date : "+str(temps)+" :"+"\n"+
                  "Les cas confirmés en France représentent "+str(percConfFr)+"% du total mondial"+"\n"+
                  "Les morts du covid19 en France représentent "+str(percDeathsFr)+"% du total mondial"+"\n"+
                  "Les guéris en France représentent "+str(percRecovFr)+"% du total mondial"+"\n"+
                  "#Covid_19 #CoronavirusFrance",in_reply_to_status_id = lastIdStatus.id) 

print(lastIdStatus.id)

lastIdStatus = api.user_timeline(screen_name = '6ita6chi6', count = 1)[0]
print(lastIdStatus.id)

api.update_status("cas covid19 confirmés en France : "+str(confirmedFrance)+"\n"+
                  "morts du covid19 en France : "+str(deathsFrance)+"\n"+
                  "guérisons totales en France "+str(recoveredFrance)+"\n"+
                  "#Covid_19 #CoronavirusFrance",in_reply_to_status_id = lastIdStatus.id)

lastIdStatus = api.user_timeline(screen_name = '6ita6chi6', count = 1)[0]

print(lastIdStatus.id)

api.update_status(
                  "cas covid19 confirmés dans le monde : "+str(totalConfirmed)+"\n"+
                  "morts du covid19 dans le monde : "+str(totalDeaths)+"\n"+
                  "guérisons totales dans le monde "+str(totalRecovered)+"\n"+
                  "#Covid_19",in_reply_to_status_id = lastIdStatus.id)


