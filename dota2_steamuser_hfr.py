#!/usr/bin/python
import requests
import json
import sys
import csv

STEAM_API_URL = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002'
STEAM_API_KEY = 'EFC5361D246BEE7B256C39D57F08ED9F'
STEAM_OPT =''
STEAM_USERNAME = ''
STEAM_ID = ''
STEAM_USERS_CSV = 'hfr_steam_users.csv'

autodialect = csv.Sniffer().sniff(file(STEAM_USERS_CSV).readline())
reader = csv.DictReader(file(STEAM_USERS_CSV), dialect=autodialect)

values =  { "hfr"   : "",
            "steam" : "",
            "id"    : "",
          }

print "[b][#FF6300]Pseudo HFR[/#FF6300] > Pseudo Steam [#888888]( ID Steam )[/#888888][/b] - [i]Passez par le profil Steam nous ajouter en amis avec l'icone[/i]"

for user in reader:
    values.update(user)
    result = ''
    if values['id']:
        result = requests.get("%s/?key=%s&steamids=%s&format=json" % (STEAM_API_URL,STEAM_API_KEY,values['id']))
        data = json.loads(result.text)
        if "personaname" in data["response"]["players"][0]:
            personaname = data["response"]["players"][0]["personaname"]
        if "avatar" in data["response"]["players"][0]:
            avatar = data["response"]["players"][0]["avatar"]
    print """[img]%s[/img] [#FF6300][b] %s [/b][/#FF6300] > [b]%s[/b] [#888888]( %s )[/#888888] [url=http://steamcommunity.com/profiles/%s][img]http://hfr-rehost.net/self/b9a108c51189de2bd6512a9156ece5e43808fabb.png[/img][/url]""" % (avatar,values['hfr'],personaname,values['id'],values['id'])

quit()
