import io
import json

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

import pandas as pd

#read API keys
with io.open('config.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

params = {
    'term': 'food',
    'limit': 20,
    'offset': 20,
    'sort': 2,
    'radius_filter': 1600
#    'category_filter': 'chinese' 
}

zipcode = 60601
#response = client.search('Chinatown, Chicago, IL'+str(zipcode), **params)
response = client.search(location = "1 E Upper Wacker Dr, Chicago, IL, 60601", **params)

BestRated = []
for business in response.businesses:
    BestRated.append([business.name,business.review_count,business.rating,business.location.coordinate.latitude,business.location.coordinate.longitude,business.location.postal_code])

for item in BestRated:
   print ('%s %d %.1f %.6f %.6f %s' %(item[0],item[1],item[2],item[3],item[4],item[5])) 

# read in Food Inspection data
df = pd.read_csv('Food_Inspections.csv', header=0)
df['Inspection Year'] = pd.to_datetime(df['Inspection Date']).apply(lambda x: x.year)

df['Zip'].fillna(0,inplace=True)
df['Zipint'] = df['Zip'].astype(int)
df['License #'].fillna(10000000,inplace=True)
df['License #'] = df['License #'].astype(int)
df['AKA Name'].fillna('missing',inplace=True)

#dflocal = df[df['Zipint']==zipcode]
dflocal = df

#dflocaltot = dflocal.groupby(['DBA Name']).count()['Results'].reset_index(name='TotIns#')
dflocaltot = dflocal.groupby(['License #']).count()['Results'].reset_index(name='TotIns#')

dflocalF = dflocal[dflocal['Results']=='Fail']
dflocalFail = dflocalF.groupby(['License #']).count()['Results'].reset_index(name='FailIns#')

y201516=dflocalF[['License #','Results']][(df['Inspection Year']>=2015)]
dflocal1516=y201516.groupby(['License #']).count()['Results'].reset_index(name='FailIns#1516')

dflocal = dflocal.merge(dflocaltot,how='outer',on='License #').merge(dflocalFail,how='outer',on='License #').merge(dflocal1516,how='outer',on='License #')

dflocal = dflocal.drop_duplicates(subset='License #', keep = 'first')
dflocal['FailIns#'].fillna(0,inplace=True) 
dflocal['FailIns#1516'].fillna(0,inplace=True) 

dflist = dflocal[['DBA Name','AKA Name','Latitude','Longitude','TotIns#','FailIns#','FailIns#1516','License #']].values.tolist()
dflist.sort()
from difflib import SequenceMatcher

def substring(s1,s2):
    if s1 in s2 or s2 in s1:
       return True
    else:
       return False 

tol = 0.001
for j in range(len(BestRated)):
    print '=====', BestRated[j][0],BestRated[j][3],BestRated[j][4]
    for i in range(len(dflist)):
        if abs(dflist[i][2] - BestRated[j][3]) < tol and abs(dflist[i][3] - BestRated[j][4]) < tol :
 #          print dflist[i][0].upper().strip(),dflist[i][1].upper().strip(),BestRated[j][0].upper().strip()
 #          print dflist[i][0],dflist[i][7],dflist[i][2],dflist[i][3] 
           seq = SequenceMatcher(None, dflist[i][0].upper().strip(), BestRated[j][0].upper().strip())
           seq2 = SequenceMatcher(None, dflist[i][1].upper().strip(), BestRated[j][0].upper().strip()) 
           if seq.ratio() > 0.8 or seq2.ratio() > 0.8 or substring(dflist[i][0].upper().strip(),BestRated[j][0].upper().strip()) or substring(dflist[i][1].upper().strip(),BestRated[j][0].upper().strip()):
               print dflist[i][0],',',dflist[i][7],',',dflist[i][4],',',dflist[i][5],',',dflist[i][6],',',BestRated[j][1],',',BestRated[j][2]
