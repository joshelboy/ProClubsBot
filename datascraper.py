# imports
import requests
from bs4 import BeautifulSoup
import sched
import time
import tweepy

s = sched.scheduler(time.time, time.sleep)

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
    currentPoints = int(scrapedData[0].text.replace("\n", "").strip())
    expectedPoints = scrapedData[1].text.replace("\n", "").strip()
    if expectedPoints != "N/A":
        expectedPoints = int(expectedPoints)
    currentMatches = int(scrapedData[2].text.replace("\n", "").strip())
    wdlStats = scrapedData[3].text.replace("\n", "").strip()  # wins,draws,loses e.g 5-1-2
    goalsScored = int(scrapedData[4].text.replace("\n", "").strip())
    goalspMatch = scrapedData[5].text.replace("\n", "").strip()
    goalsConceded = int(scrapedData[6].text.replace("\n", "").strip())
    gcpMatch = scrapedData[7].text.replace("\n", "").strip()
    goalsDifference = int(scrapedData[8].text.replace("\n", "").strip())
    plMatches = scrapedData[9].text.replace("\n", "").strip()  # punkte der letzten 6 spiele
    playedMatches = int(scrapedData[10].text.replace("\n", "").strip())

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
    consumerKey = "secret"
    consumerKeySecret = "secret"
    accessToken = "secret"
    accessTokenSecret = "secret"

    auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except:
        print("Error during authentication")
    goals = goalsScored - oldScored
    conceded = goalsConceded - oldConceded
    if currentPoints == oldCurrent and currentMatches != oldCurrent:
        if currentMatches == 1:
            try:
                api.update_status("Ärgerlich! Gleich im ersten Spiel war unser Spielfluss bei weitem nicht so Weltklasse, wie Max Meyer. Wir verlieren mit: " + str(goals) + "-" + str(conceded))
            except:
                print("Error 18")
        if currentMatches > 1:
            try:
                api.update_status("Das " + str(currentMatches) + ". Spiel geht leider an unsere Gegner. Wir verlieren mit " + str(goals) + "-" + str(conceded))
            except:
                print("Error 18")
    if currentPoints != oldPoints and currentMatches != oldCurrent:
        if currentPoints == oldPoints + 3:
            if currentMatches == 1:
                try:
                    api.update_status("Auftakt Sieg! Völlig sicher schippert WsmdnS United richtung Siegeshafen. Ein müheloser " + str(goals) + "-" + str(conceded) + " Sieg.")
                except:
                    print("Error 18")
            if currentMatches > 1:
                try:
                    api.update_status("Das " + str(currentMatches) + ". Spiel geht natürlich an uns. Wir gewinnen mit " + str(goals) + "-" + str(conceded))
                except:
                    print("Error 18")
        if currentPoints == oldPoints + 1:
            if currentMatches == 1:
                try:
                    api.update_status("Ein für unsere Verhältnisse gelungener Auftakt! Wie von Xylence gewünscht spielen wir Unentschieden. Das Endergebnis ist: " + goals + "-" + conceded)
                except:
                    print("Error 18")
            if currentMatches < 1:
                print("Punktteilung im " + str(currentMatches) + ". Spiel. Die Anzeigetafel zeigt ein " + str(goals) + "-" + str(conceded))

def loop(sc):
    update()
    scrapeData()
    compare()
    s.enter(30, 1, loop, (sc,))

def main():
    scrapeData()
    s.enter(30, 1, loop, (s,))
    s.run()

main()
