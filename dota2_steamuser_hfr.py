#!/usr/bin/python
# -*- coding: cp1252 -*-
import requests
import json
import sys
import csv
from urllib2 import urlopen
from wand.image import Image
import PIL
from PIL import ImageFont
from PIL import Image as ImagePIL
from PIL import ImageDraw

STEAM_API_URL = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002'
STEAM_API_KEY = '87574B731CF28200DCBF34BFFC4A152A'
STEAM_OPT =''
STEAM_USERNAME = ''
STEAM_ID = ''
STEAM_USERS_CSV = 'hfr_steam_users.csv'

autodialect = csv.Sniffer().sniff(file(STEAM_USERS_CSV).readline())
reader = csv.DictReader(file(STEAM_USERS_CSV), dialect=autodialect)

values =  { "hfr"   : "",
            "steam" : "",
            "id"    : "",
            "rank"  : "",
          }

for user in reader:
    background = Image(filename='fond.png')
    values.update(user)
    result = ''
    if values['id']:
        result = requests.get("%s/?key=%s&steamids=%s&format=json" % (STEAM_API_URL,STEAM_API_KEY,values['id']))
        data = json.loads(result.text)
        if "personaname" in data["response"]["players"][0]:
            personaname = data["response"]["players"][0]["personaname"][:20]
        if "avatar" in data["response"]["players"][0]:
            avatar = data["response"]["players"][0]["avatar"]
            loadedimg = urlopen(avatar)
            userimg = Image(file=loadedimg)
            loadedimg.close()
            rankimg=Image(filename='rank%s.png' % values["rank"])
            background.composite(userimg,6,6)
            background.composite(rankimg,224,6)
        background.format = 'png'
        background.save(filename='%s.png' % values["id"])
        font = ImageFont.truetype("UbuntuMono-R.ttf",17)
        img=ImagePIL.open('%s.png' % values["id"])
        draw = ImageDraw.Draw(img)
        draw.text((44, 23),"%s" % (personaname),(255,255,255),font=font)
        draw = ImageDraw.Draw(img)
        draw.text((44, 3),"%s" % (values['hfr'][:20]),(241,143,24),font=font)
        draw = ImageDraw.Draw(img)
        img.save('%s.png' % values["id"])
        print "%s's image created." % (values['hfr'])
quit()

