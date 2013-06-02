#!/usr/bin/python
import csv
import sys

STEAM_USERS_CSV = 'hfr_steam_users.csv'

autodialect = csv.Sniffer().sniff(file(STEAM_USERS_CSV).readline())
reader = csv.DictReader(file(STEAM_USERS_CSV), dialect=autodialect)

for user in reader:
        steamid = user["id"]
        sys.stdout.write("""[url=http://steamcommunity.com/profiles/%s][img]https://github.com/NunursMegaPower/HFR-Dota2/blob/master/%s.png?raw=true[/img][/url]""" % (steamid,steamid))
        if not((reader.line_num-1)%3):print
quit()
