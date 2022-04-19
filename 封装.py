import ast
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

url2019 = 'https://store.steampowered.com/sale/2019_top_sellers'
url2020 = 'https://store.steampowered.com/sale/BestOf2020?tab=4'
url2021 = 'https://store.steampowered.com/sale/BestOf2021?tab=1'
def GetSteamYearGamesInfo(url):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        config = soup.find(id="application_config") #提取id=application_config
        games_info_json = json.loads(config['data-applinkinfo']) #json解析器解析data-applinkinfo属性,string->list&dict
        return games_info_json
    else:
        return None

def GetGamesNameList(games_info):
    return [game['title'] for game in games_info]

def GetGamesIdList(games_info):
    return [game['appid'] for game in games_info]

def FormatGameInfo(game_info):
    return [game_info['appid'],game_info['title'],json.dumps(game_info['tags'])]

def ShowGamesInfo(games_info):
    arr = []
    for game in games_info:
        #s = ', '.join([x['name'] for x in game['tags']])
        s = ([x['name'] for x in game['tags']])
        #print('{:<10}{:<50}{}'.format(game['appid'],game['title'],s))
        #return s
        #print (s)
        arr.append(s)
    return(arr)

def ConvertToDF(games_info):
    return pd.DataFrame([[game_info['appid'],game_info['title'],json.dumps(game_info['tags'])] for game_info in games_info])

def GetReviewOfGameId(id,filter='all',language='english',day_range=1000,cursor='*',review_type='all',purchase_type='all',num_per_page=100):
    prefix = 'https://store.steampowered.com/appreviews/'
    res = requests.get(prefix+str(id),params={'json':1,'filter':filter,'language':language,'day_range':day_range,
    'cursor':cursor,'review_type':review_type,'purchase_type':purchase_type,'num_per_page':num_per_page})

    if res.status_code == 200:
        return res.json()
    else:
        return None


'''
count = 1
stra = GetReviewOfGameId(271590)['reviews']
for i in range (0,100):
    strb = stra[i]['review']
    # lista = list(stra.split(" "))
    print(count,'条评论\n',strb )
    count += 1
'''
'''

import time
arr = []
cursor = '*'
count = 1
for i in range (0,100):
    review = GetReviewOfGameId(271590,cursor = cursor, num_per_page=100)
    cursor = review ['cursor']
    arr += review ['reviews']
    if review ['success'] != 1:
        print (review)
        break
    if int(review['query_summary']['num_reviews']) != 100:
        break
    print('review count:'+ str(len(arr)))
    time.sleep(0.5)

for x in range (0,100000):
    print(x,'条评论\n',arr[x]['review'])


# print(len(arr))
'''





#print(GetReviewOfGameId(271590)['reviews'])


#games_info = GetSteamYearGamesInfo(url2019)
#print(ConvertToDF(games_info).head())

games_info2020 = GetSteamYearGamesInfo(url2020)
games_info2019= GetSteamYearGamesInfo(url2019)
games_info2021= GetSteamYearGamesInfo(url2021)
GetGamesNameList(games_info2020)
GetGamesIdList(games_info2020)

#FormatGameInfo(game_info)
#ShowGamesInfo(games_info2020)

GetGamesNameList(games_info2019)
GetGamesIdList(games_info2019)
#FormatGameInfo(game_info)
#ShowGamesInfo(games_info2019)

GetGamesNameList(games_info2021)
GetGamesIdList(games_info2021)
#FormatGameInfo(game_info)
#ShowGamesInfo(games_info2021)

print (games_info2021)
#totaltags = ShowGamesInfo(games_info2020) + ShowGamesInfo(games_info2019) + ShowGamesInfo(games_info2021)
#print (totaltags)


'''
file = open('tags.txt','w')
file.write('.'.join(totaltags))

file.close()
'''
'''
    for key in config.attrs.keys():
        print(key)
'''

