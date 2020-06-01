#imports
import requests
from bs4 import BeautifulSoup

#Aufrufen der Website
page = requests.get("https://proclubshead.com/20/club/ps4-23063893/")
soup = BeautifulSoup(page.content,"html.parser")


#Scraping Data Methode, weil EA keine API rausgibt

#Aktuelle Punktzahl wird in "currentPoints" gespeichert
#.text.replace("\n","").strip() -> replaced und formatiert das ganze zu einem rohen Text
#...also werden Dinge, wie <div [...]> entfernt
scrapedData = soup.find_all("span",{"class":"font-weight-bold ml-1"})

#speichern der einzelnen Elemente der ArrayList
currentPoints = scrapedData[0]
expectedPoints = scrapedData[1]
playedMatches = scrapedData[2]
wdlStats = scrapedData[3] #wins,draws,loses e.g 5-1-2
goalsScored = scrapedData[4]
goalspMatch = scrapedData[5]
goalsConceded = scrapedData[6]
gcpMatch = scrapedData[7]
goalsDifference = scrapedData[8]
plMatches = scrapedData[9] #punkte der letzten 6 spiele
playedMatches = scrapedData[10]

#aktuelle Liga
currentPoints = soup.find("span",{"class":"font-weight-bold ml-1"}).text.replace("\n","").strip()

print("Aktuelle Punktzahl:" + currentPoints)
