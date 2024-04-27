# -*- coding: utf-8 -*-
import telebot
from telebot import types
import requests
import re
from datetime import datetime
import time,string,random,datetime 
from requests import get, exceptions
import json
from os.path import getsize
import random
import string
from requests_toolbelt import MultipartEncoder
import vk_api
from bs4 import BeautifulSoup
from threading import Thread
import threading
from telethon import TelegramClient, events
from telethon.tl.functions.messages import ForwardMessagesRequest,SendMessageRequest
from telethon import TelegramClient, sync, events
import json
import time
from telethon.tl.types import MessageMediaWebPage,MessageEntityBold
from telethon import TelegramClient
from telethon import TelegramClient, events
import telethon.tl.types
import os


api_id =  ##api id telegram
api_hash = '' ##api_hash telegram
token = ''   # токен api vk.com
group_id = '' # id группы vk.com / страницы профиля
client = TelegramClient("session", api_hash=api_hash, api_id=api_id)
name1 = 'Красивые девушки #красотки #блондинки #девушки #секси #малышки #голые #развратные #попки #сиськи'
discr = '#красотки #блондинки #девушки #секси #малышки #голые #развратные #попки #сиськи'
filename = 'videos.mp4'

def gooooog(sed):
 lol=sed
 get_video_upload_url2 = requests.post("https://api.vk.com/method/video.save?v=5.231&client_id=7879029", data=dict(
                                                                               group_id=group_id,
                                                                               file_size=getsize(filename),
                                                                               description=discr,
                                                                               wallpost=0,
                                                                               name=name1,
                                                                               access_token=token),verify=False).text
 ffd = re.search(r'"upload_url":"(.*?)","video_id',str(get_video_upload_url2)).group()
 ffd = ffd.replace('"upload_url":"','').replace('","video_id','').replace('\/','/')
 files = {
    'file': ('videos.mp4', open('videos.mp4', 'rb')),
 }        
 r2 = requests.post(ffd, files=files)
 
 name2 = 'Красивые девушки #красотки #блондинки #девушки #секси #малышки #голые #развратные #попки #сиськи'
 disc2r = '#красотки #блондинки #девушки #секси #малышки #голые #развратные #попки #сиськи'

 headesr = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0',
            'Origin':'https://vk.com',
            'Cookie':'you cookie'}  ## вставить куки после авторизации
 get_video_upload_url2w = requests.post("https://login.vk.com/?act=web_token",data=dict(version='1',app_id='6287487',access_token=token),verify=False,headers=headesr).text

                                                                               
 ffd00 = re.search(r'"access_token":"(.*?)","expires":',str(get_video_upload_url2w)).group()
 ffd00 = ffd00.replace('"access_token":"','').replace('","expires":','').replace('\/','/')



 get_video_upload_url2www = requests.post("https://api.vk.com/method/shortVideo.create?v=5.231&client_id=6287487", data=dict(
                                                                               group_id=group_id,
                                                                               file_size=getsize(filename),
                                                                               description=name2,
                                                                               wallpost=1,
                                                                               access_token=ffd00),verify=False).text  

 ffd2222 = re.search(r'"upload_url":"(.*?)"}}',str(get_video_upload_url2www)).group()
 ffd2222 = ffd2222.replace('"upload_url":"','').replace('"}}','').replace('\/','/')
 ffdhashh = re.search(r'&vkVideoHash=(.*?)"}}',str(get_video_upload_url2www)).group()
 ffdhashh = ffdhashh.replace('&vkVideoHash=','').replace('"}}','').replace('\/','/')
 files11 = {
    'file': ('videos1.mp4', open('videos1.mp4', 'rb')),
 }        
 r2www = requests.post(ffd2222, files=files11)
                                                                          
 ffd1 = re.search(r'"owner_id":(.*?),"video_id"',str(get_video_upload_url2www)).group()
 ffd1 = ffd1.replace('"owner_id":','').replace(',"video_id"','').replace('\/','/')
 ffd12 = re.search(r'"video_id":(.*?),"upload_url"',str(get_video_upload_url2www)).group()
 ffd12 = ffd12.replace('"video_id":','').replace(',"upload_url"','').replace('\/','/')
 time.sleep(5)
 params222 = {
         'video_id':ffd12,
         'owner_id':ffd1,
         'description':name2,
         'privacy_view':'all',
         'privacy_comment':'all',
         'publish_date':'0',
         'audio_raw_id':'',
         'ord_info':'{"is_ads":false,"advertisers":[]}',
         'access_token':ffd00,
         'privacy_view':'all',    
 } 
 get_video_upload_url2000 = requests.post("https://api.vk.com/method/shortVideo.edit?v=5.231",data=params222,verify=False).text
 time.sleep(5)
 data2 = dict(video_id=ffd12,owner_id=ffd1,wallpost=1,license_agree=1,publish_date=0,ref='clips_viewer',access_token=ffd00)
 rqz =requests.post('https://api.vk.com/method/shortVideo.publish?v=5.231',data=data2,verify=False).text

@client.on(events.NewMessage())
async def newMessageListener(event):
   sender = "-100{}".format(event.message.chat.id)
   if str(sender) == '-000000000000': #telegram канал откуда парсится контент 
     file_name = "videos.mp4"
     file_name2 = "videos1.mp4"
     await event.download_media(file_name)
     print("New VIDEO [VIDEO]")
     await event.download_media(file_name2)
     print("New VIDEO [SHORTS]")
     gooooog(sender)

with client.start():
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
