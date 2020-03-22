#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:36:13 2020

@author: bernardintheo
"""

from covid import Covid
from main import ecritureXLSX
import datetime



temps = datetime.datetime.now()



covid = Covid()

# _______________________________________________________________
#|                                                              |
#|                          DANS LE MONDE                       |  
#|______________________________________________________________| 

totalConfirmed = covid.get_total_confirmed_cases()
totalRecovered = covid.get_total_recovered()
totalDeaths = covid.get_total_deaths()


# _______________________________________________________________
#|                                                              |
#|                          EN FRANCE                           |  
#|______________________________________________________________|

percFR = []

confirmedFrance = covid.get_status_by_country_name("france")['confirmed']
deathsFrance = covid.get_status_by_country_name("france")['deaths']
recoveredFrance = covid.get_status_by_country_name("france")['recovered']

percConfFr = round((confirmedFrance/totalConfirmed)*100,2)
percDeathsFr = round((deathsFrance/totalDeaths)*100,2)
percRecovFr = round((recoveredFrance/totalRecovered)*100,2)

percFR.append([temps,'France',percConfFr,percDeathsFr,percRecovFr])

# _______________________________________________________________
#|                                                              |
#|                          EN ITALIE                           |  
#|______________________________________________________________| 

percIt = []

confirmedItaly = covid.get_status_by_country_name("italy")['confirmed']
deathsItaly = covid.get_status_by_country_name("italy")['deaths']
recoveredItaly = covid.get_status_by_country_name("italy")['recovered']

percConfIt = round((confirmedItaly/totalConfirmed)*100,2)
percDeathsIt = round((deathsItaly/totalDeaths)*100,2)
percRecovIt = round((recoveredItaly/totalRecovered)*100,2)

percIt.append([temps,'Italie',percConfIt,percDeathsIt,percRecovIt])


# _______________________________________________________________
#|                                                              |
#|                          EN ESPAGNE                          |  
#|______________________________________________________________| 

percEs = []

confirmedEspagne = covid.get_status_by_country_name("spain")['confirmed']
deathsEspagne = covid.get_status_by_country_name("spain")['deaths']
recoveredEspagne = covid.get_status_by_country_name("spain")['recovered']

percConfEs = round((confirmedEspagne/totalConfirmed)*100,2)
percDeathsEs = round((deathsEspagne/totalDeaths)*100,2)
percRecovEs = round((recoveredEspagne/totalRecovered)*100,2)

percEs.append([temps,'Espagne',percConfEs,percDeathsEs,percRecovEs])



# _______________________________________________________________
#|                                                              |
#|                          EN ALLEMAGNE                        |  
#|______________________________________________________________| 

percAll = []

confirmedAllemagne = covid.get_status_by_country_name("germany")['confirmed']
deathsAllemagne = covid.get_status_by_country_name("germany")['deaths']
recoveredAllemagne = covid.get_status_by_country_name("germany")['recovered']

percConfAll = round((confirmedAllemagne/totalConfirmed)*100,2)
percDeathsAll = round((deathsAllemagne/totalDeaths)*100,2)
percRecovAll = round((recoveredAllemagne/totalRecovered)*100,2)

percAll.append([temps,'Allemagne',percConfAll,percDeathsAll,percRecovAll])



# _______________________________________________________________
#|                                                              |
#|                          EN ANGLETERRE                       |  
#|______________________________________________________________| 

percUk = []

confirmedUk = covid.get_status_by_country_name("united kingdom")['confirmed']
deathsUk = covid.get_status_by_country_name("united kingdom")['deaths']
recoveredUk = covid.get_status_by_country_name("united kingdom")['recovered']

percConfUk = round((confirmedUk/totalConfirmed)*100,2)
percDeathsUk = round((deathsUk/totalDeaths)*100,2)
percRecovUk = round((recoveredUk/totalRecovered)*100,2)

percUk.append([temps,'UK',percConfUk,percDeathsUk,percRecovUk])



percDiffMdConf = 100-(percConfFr+percConfIt+percConfEs+percConfAll+percConfUk)
percDiffMdMorts = 100-(percDeathsFr+percDeathsIt+percDeathsEs+percDeathsAll+percDeathsUk)
percDiffMdGueris = 100-(percRecovFr+percRecovIt+percRecovEs+percRecovAll+percRecovUk)


ec = ecritureXLSX()

ec.ecrireXLSX('data/donneesCorona.xlsx','percent',[[temps,'France',percConfFr,percDeathsFr,percRecovFr]])
ec.ecrireXLSX('data/donneesCorona.xlsx','percent',[[temps,'Italie',percConfIt,percDeathsIt,percRecovIt]])
ec.ecrireXLSX('data/donneesCorona.xlsx','percent',[[temps,'Espagne',percConfEs,percDeathsEs,percRecovEs]])
ec.ecrireXLSX('data/donneesCorona.xlsx','percent',[[temps,'Allemagne',percConfAll,percDeathsAll,percRecovAll]])
ec.ecrireXLSX('data/donneesCorona.xlsx','percent',[[temps,'UK',percConfUk,percDeathsUk,percRecovUk]])
ec.ecrireXLSX('data/donneesCorona.xlsx','percent',[[temps,'Reste du monde',percDiffMdConf,percDiffMdMorts,percDiffMdGueris]])