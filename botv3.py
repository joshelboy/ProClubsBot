import requests
import json
headers = {'Host': 'proclubs.ea.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
           'Accept': 'application/json',
           'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate, br',
           'Origin': 'https://www.ea.com',
           'Connection': 'keep-alive',
           'Referer': 'https://www.ea.com/de-de/games/fifa/fifa-20/pro-clubs/overview?clubId=23063893&platform=ps4',
           'TE': 'Trailers',
           'Pragma': 'no-cache',
           'Cache-Control': 'no-cache'}

liga = "https://proclubs.ea.com/api/fifa/clubs/matches?platform=ps4&clubIds=23063893&matchType=gameType9&maxResultCount=1"
clubStats = "https://proclubs.ea.com/api/fifa/clubs/seasonalStats?platform=ps4&clubIds=23063893"
infos = "https://proclubs.ea.com/api/fifa/clubs/info?platform=ps4&clubIds=23063893"
r = requests.get(clubStats, headers=headers)
load = r.content.strip().decode()
clubStats = json.loads(load)
stats = clubStats[0]
season = stats.get('seasons')
titlesWon = stats.get('titlesWon')
leaguesWon = stats.get('leaguesWon')
promotions = stats.get('promotions')
holds = stats.get('holds')
relegations = stats.get('relegations')

# 0 = Niederlage, 1 = Tie, 2= Sieg
letztesSpiel = stats.get('lastMatch0')
vorletztesSpiel = stats.get('lastMatch1')

allTimeGoals = stats.get("alltimeGoals")
allTimeGames = stats.get('totalGames')

seasonWins = stats.get('seasonWins')
seasonTies = stats.get('seasonTies')
seasonLosses = stats.get('seasonLosses')

gamesPlayed = stats.get('gamesPlayed')
goals = stats.get('goals')
goalsAgainst = stats.get('goalsAgainst')
points = stats.get('points')
print(season)
print(clubStats)
#name = allgemein["name"]
#print(name)
