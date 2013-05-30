#!/usr/bin/python
import requests
import json

STEAM_API_URL = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002'
STEAM_API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
STEAM_USERNAME = ''
STEAM_ID = '76561197960739468'

result = requests.get("%s/?key=%s&steamids=%s&format=json" % (STEAM_API_URL,STEAM_API_KEY,STEAM_ID))
data = json.loads(result.text)
avatar = data["response"]["players"][0]["avatar"]
print avatar
