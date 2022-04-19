# Steam API

import ast
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd



def GetReviewOfGameId(id,filter='all',language='english',day_range=626.75,cursor='*',review_type='all',purchase_type='all',num_per_page=20):
    prefix = 'https://store.steampowered.com/appreviews/'
    res = requests.get(prefix+str(id),params={'json':1,'filter':filter,'language':language,'day_range':day_range,
    'cursor':cursor,'review_type':review_type,'purchase_type':purchase_type,'num_per_page':num_per_page}) #,
    if res.status_code == 200:
        return res.json()
    else:
        return None

arr = []
cursor = '*'
for i in range(0,100):
    review = GetReviewOfGameId(271590,cursor=cursor,num_per_page=100)
    cursor = review['cursor']
    arr += review['reviews']
    if review['success'] != 1:
        print(review)
        break
    if review['query_summary']['num_reviews'] != 100:
        break
    print('Review Count: '+str(len(arr)))

abc = []
# print(len(arr))
for x in range (0,13000):
    if x >10000:
        abc.append ([arr[x]['review']])
    # print(x,'条评论\n',arr[x]['review'])
    #print(type(arr[x]['review']))


bcd = str(abc)

file = open('第三.txt','w', encoding="utf-8")
file.write(bcd)

file.close()


# Metacritic API
import requests from bs4
import BeautifulSoup
#import time
#import random as rand
import pandas as pd
review_dict = {'name':[], 'date':[], 'rating':[], 'review':[]}
review_dict = {'name':[], 'date':[], 'rating':[], 'review':[]}

for page in range(0,12): #Remember to update the number of pages
    url = 'https://www.metacritic.com/game/pc/grand-theft-auto-v/user-reviews/user-reviews?page='+str(page)
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = requests.get(url, headers = user_agent)
    #time.sleep(rand.randint(3,30))
    soup = BeautifulSoup(response.text, 'html.parser')
    for review in soup.find_all('div', class_='review_content'):
        if review.find('div', class_='name') == None:
                       break
        review_dict['name'].append(review.find('div', class_='name').find('a').text)
        review_dict['date'].append(review.find('div', class_='date').text)
        review_dict['rating'].append(review.find('div', class_='review_grade').find_all('div')[0].text)
        if review.find('span', class_='blurb blurb_expanded'):
            review_dict['review'].append(review.find('span', class_='blurb blurb_expanded').text)
        else:
            review_dict['review'].append(review.find('div', class_='review_body').find('span').text)

gta_reviews = pd.DataFrame(review_dict)

#Reddit API
import requests
import jsonpath

'''reddit official api method
client_id='55vVoa0UQ4hFaB2xp6Qliw'
secret_key='o_NM8lXya7AIvvS6BMYc_R9EshNYaQ'

auth = requests.auth.HTTPBasicAuth(client_id,secret_key) #创建的key
data ={
    'grant_type':'password',
    'username':'xbw199942',
    'password':'Xbw891054582'
} #reddit的账户名称和密码

headers ={'User-Agent':'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                  auth=auth,data=data,headers=headers) #登录

TOKEN = res.json()['access_token']

headers={**headers, **{'Authorization':f'bearer{TOKEN}'}}

headers

res = requests.get('https://oauth.reddit.com/r/python/hot', headers=headers)
'''


url1='https://api.pushshift.io/reddit/comment/search/?q=gtav&size=450&before=270d'
res1=requests.get(url1)
res1

need = jsonpath.jsonpath(res1.json(),'$..body')

