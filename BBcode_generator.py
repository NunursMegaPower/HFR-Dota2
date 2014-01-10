#!/usr/bin/python
import csv
import sys

STEAM_USERS_CSV = 'tournoi_hfr_steam_users.csv'

autodialect = csv.Sniffer().sniff(file(STEAM_USERS_CSV).readline())
reader = csv.DictReader(file(STEAM_USERS_CSV), dialect=autodialect)

for user in reader:
        hfrname = user["hfr"]
        steamid = user["id"]
        sys.stdout.write("""[url=http://steamcommunity.com/profiles/%s][img title=%s]https://github.com/NunursMegaPower/HFR-Dota2/blob/master/%s.png?raw=true[/img][/url]""" % (steamid,hfrname,steamid))
        if not((reader.line_num-1)%4):print
quit()
