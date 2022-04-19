import ast
import requests
import jsonfrom

bs4
import BeautifulSoup
import pandas as pd

url2019 = 'https://store.steampowered.com/sale/2019_top_sellers'
url2020 = 'https://store.steampowered.com/sale/BestOf2020?tab=4'
url2021 = 'https://store.steampowered.com/sale/BestOf2021?tab=1'


def GetSteamYearGamesInfo(url):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        config = soup.find(id="application_config")
        games_info_json = json.loads(config['data-applinkinfo'])
    else:
        return None


def GetGamesNameList(games_info):
    return [game['title'] for game in games_info]


def GetGamesIdList(games_info):
    return [game['appid'] for game in games_info]


def FormatGameInfo(game_info):
    return [game_info['appid'], game_info['title'], json.dumps(game_info['tags'])]


def ShowGamesTag(games_info):
    arr = []
    for game in games_info:
        s = ([x['name'] for x in game['tags']])
        arr.append(s)
        return (arr)


def ShowGamesInfo(games_info):
    arr = []
    for game in games_info:
        s = ', '.join([x['name'] for x in game['tags']])
        print('{:<10}{:<50}{}'.format(game['appid'], game['title'], s))


def ConvertToDF(games_info):
    return pd.DataFrame(
        [[game_info['appid'], game_info['title'], json.dumps(game_info['tags'])] for game_info in games_info])


games_info2020 = GetSteamYearGamesInfo(url2020)
games_info2019 = GetSteamYearGamesInfo(url2019)
games_info2021 = GetSteamYearGamesInfo(url2021)
GetGamesNameList(games_info2020)
GetGamesIdList(games_info2020)

# FormatGameInfo(game_info)
ShowGamesInfo(games_info2020)

GetGamesNameList(games_info2019)
GetGamesIdList(games_info2019)
# FormatGameInfo(game_info)
ShowGamesInfo(games_info2019)

GetGamesNameList(games_info2021)
GetGamesIdList(games_info2021)
# FormatGameInfo(game_info)
ShowGamesInfo(games_info2021)

totaltags = ShowGamesTag(games_info2020) + ShowGamesTag(games_info2019) + ShowGamesTag(games_info2021)
print(totaltags)
