# imports
import requests
from bs4 import BeautifulSoup
import sched
import time

zero = 0
one = 1
three = 3


def scrapeData():
    page = requests.get("https://proclubshead.com/20/club/ps4-23063893/")
    soup = BeautifulSoup(page.content, "html.parser")

    # Scraping Data Methode, weil EA keine API rausgibt

    # Aktuelle Punktzahl wird in "currentPoints" gespeichert
    # .text.replace("\n","").strip() -> replaced und formatiert das ganze zu einem rohen Text
    # ...also werden Dinge, wie <div [...]> entfernt
    scrapedData = soup.find_all("span", {"class": "font-weight-bold ml-1"})

    global currentPoints
    global expectedPoints
    global currentMatches
    global wdlStats
    global goalsScored
    global goalspMatch
    global goalsConceded
    global gcpMatch
    global goalsDifference
    global plMatches
    global playedMatches


    # speichern der einzelnen Elemente der ArrayList
    currentPoints = scrapedData[0].text.replace("\n", "").strip()
    expectedPoints = scrapedData[1].text.replace("\n", "").strip()
    currentMatches = scrapedData[2].text.replace("\n", "").strip()
    wdlStats = scrapedData[3].text.replace("\n", "").strip()  # wins,draws,loses e.g 5-1-2
    goalsScored = scrapedData[4].text.replace("\n", "").strip()
    goalspMatch = scrapedData[5].text.replace("\n", "").strip()
    goalsConceded = scrapedData[6].text.replace("\n", "").strip()
    gcpMatch = scrapedData[7].text.replace("\n", "").strip()
    goalsDifference = scrapedData[8].text.replace("\n", "").strip()
    plMatches = scrapedData[9].text.replace("\n", "").strip()  # punkte der letzten 6 spiele
    playedMatches = scrapedData[10].text.replace("\n", "").strip()

def update():
    global oldPoints
    global oldExpected
    global oldCurrent
    global oldWdl
    global oldScored
    global oldsMatch
    global oldConceded
    global oldcMatch
    global oldDifference
    global oldpMatches
    global oldMatches

    oldPoints = currentPoints
    oldExpected = expectedPoints
    oldCurrent = currentMatches
    oldWdl = wdlStats
    oldScored = goalsScored
    oldsMatch = goalspMatch
    oldConceded = goalsConceded
    oldcMatch = gcpMatch
    oldDifference = goalsDifference
    oldpMatches = plMatches
    oldMatches = playedMatches

def compare():
    if currentPoints == oldPoints:
        print("Lose")

    if currentPoints != oldPoints:
        if currentPoints == oldPoints + three:
            print("Sieg")

def loop():
    update()
    scrapeData()
    compare()

def main():
    scrapeData()
    loop()
    print(oldPoints)

main()
