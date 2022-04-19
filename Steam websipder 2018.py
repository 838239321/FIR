import requests as r
import json
from bs4 import BeautifulSoup
import pandas as pd

res = r.get('https://store.steampowered.com/sale/2018_so_far_top_sellers/')

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    config = soup.find_all('div',{'class' : 'item'}) #提取id=application_config


    #j_app_info = json.loads(config['data-applinkinfo']) #json解析器解析data-applinkinfo属性,string->list&dict
    count=100
    for app in config:
         print('\tappid: '+str(app['data-ds-appid']) + '\ttags: ' + app['data-ds-tagids'])

    # appid = app['appid']
    # title = app['title']
    # tags = s
    # df = pd.DataFrame(columns=['appid', 'title', 'tags'])
    # arr = pd.DataFrame([app['appid'],app['title'],s],columns=['appid', 'title', 'tags'])
    # #df = pd.concat([df,arr])
    #     arr = pd.DataFrame(
    #         [[game_info['appid'], game_info['title'], json.dumps(game_info['tags'])] for game_info in j_app_info])


    # print(arr[1])
    # arr.to_csv('123.csv')