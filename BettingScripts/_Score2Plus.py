from sgmllib import SGMLParser
import string
import datetime
import time
from datetime import timedelta

now = datetime.datetime.now()
day2 = now + datetime.timedelta(days=1)
day3 = now + datetime.timedelta(days=2)
day4 = now + datetime.timedelta(days=3)
day5 = now + datetime.timedelta(days=4)

today = now.strftime("%A")
day2 = day2.strftime("%A")
day3 = day3.strftime("%A")
day4 = day4.strftime("%A")
day5 = day5.strftime("%A")

today = today.lower()
day2 = day2.lower()
day3 = day3.lower()
day4 = day4.lower()
day5 = day5.lower()

gamesTotal = 0
gamesValid = 0
totalValid = 0
singleBet = 0

def getData():
    global gamesTotal
    global gamesValid
    global totalValid
    global singleBet

    #Skip if only 1 bet or limited type as will not have +2 Goals bet        
    if (test.find(' 1 Bet ') != -1) \
        or (test.find(' 2 Bets ') != -1)\
        or (test.find(' 3 Bets ') != -1)\
        or (test.find(' 4 Bets ') != -1)\
        or (test.find(' 5 Bets ') != -1)\
        or (test.find(' 6 Bets ') != -1)\
        or (test.find(' 7 Bets ') != -1)\
        or (test.find(' 8 Bets ') != -1)\
        or (test.find(' 9 Bets ') != -1)\
        or (test.find(' 10 Bets ') != -1)\
        or (test.find(' 11 Bets ') != -1)\
        or (test.find(' 12 Bets ') != -1)\
        or (test.find(' 13 Bets ') != -1)\
        or (test.find(' 14 Bets ') != -1)\
        or (test.find(' 15 Bets ') != -1)\
        or (test.find(' 16 Bets ') != -1)\
        or (test.find(' 17 Bets ') != -1)\
        or (test.find(' 18 Bets ') != -1)\
        or (test.find(' 19 Bets ') != -1)\
        or (test.find(' 20 Bets ') != -1):
        singleBet = 1
        #print test
        
    
    if test.find('class="all-bets-toggle"') != -1 and singleBet == 0:
        doublechance = test
        doublechance = doublechance.strip()
        doublechance = doublechance[34:]
        doublechance = doublechance[:-36]
        doublechance = "https://www.skybet.com" + doublechance
        if doublechance.find('football-live') == -1:
            sock2 = urllib.urlopen(doublechance)
            htmlSource1 = sock2.read()
            sock2.close()
            #Check to see if the page is valid and then continue:
            #if htmlSource.find('<html') != -1:
            xits = 2
            if xits != 1 :
                logfile1 = open("temp2.log", 'w') #This adds to a file to read easier
                logfile1.write(htmlSource1)
                logfile1.close()
                #Read line by line adding one each time
                g = open ("temp2.log", "rb")
                for k in range (1, 20000, 1):
                    test1 = g.readline()

                    #get fixture details
                    if test1.find('data-event-headline') != -1:
                        test1 = g.readline()
                        fix = test1.strip()
                        fix = fix[1:]
                        fix = fix[:-5]
                        fixteams = fix.split(' v ')
                        #print fixteams[0]
                        #print fixteams[1]
                        team2back = fixteams[0]

                    #Gets Fixture Details
                    if test1.find('<h2 class="event-title sub-head">') != -1:
                        test1 = g.readline()
                        test1 = g.readline()
                        fixdet = test1.strip()
                        fixdet = fixdet.split('|')
                        #print fixdet[2]
                        #print fixdet[2]

                    #get shortcut if it is a Handicap -1 game in prep.
                    if test1.find('span data-market-id') != -1:
                        dc = test1.split('"')
                        #print test1.strip()

                    if test1.find('To Score 2+ Goals') != -1:
                        #print test1.strip()
                        dclink = dc[1]
                        #print dc[1]
                        t = 1
                        hdw = 1
                        hdwstring = "[H]"
                        while t == 1:
                            test1 = g.readline()
                            if test1.find('"nofollow"') != -1:
                                test1 = test1.strip()
                                #1/1, 11/8, 13/10, 13/8, 6/4, 11/10, 6/5, 5/4, 4/3
                                gamesTotal = gamesTotal + 1
                                if (test1.find('data-oc-price-num="30" data-oc-price-den="100"') != -1) \
                                    or (test1.find('data-oc-price-num="1" data-oc-price-den="3"') != -1) \
                                    or (test1.find('data-oc-price-num="2" data-oc-price-den="5"') != -1) \
                                    or (test1.find('data-oc-price-num="2" data-oc-price-den="9"') != -1) \
                                    or (test1.find('data-oc-price-num="1" data-oc-price-den="4"') != -1) \
                                    or (test1.find('data-oc-price-num="2" data-oc-price-den="7"') != -1) \
                                    or (test1.find('data-oc-price-num="4" data-oc-price-den="11"') != -1):
                                    #print test
                                    #print test1

                                    gamehyper = test.split('"')
                                    gamedata = test1.split('"')
                                    #print gamehyper[3]

                                    gamelink = "http://www.skybet.com" + gamehyper[3]
                                    gamelink = gamelink.strip()


                                    #print gamedata[7]
                                    #print gamedata[9]
                                    #print gamedata[15]

                                    #print gamedata[15],gamedata[7],"/",gamedata[9]
                                    #print gamelink
                                    gamewrite = team2back + " " + gamedata[7] + "/" + gamedata[9]

                                    print gamewrite
                                    print gamelink
                                    print "---------"

                                    league = gamelink.split('/')
                                    #print league[4]
                                    gamesValid = gamesValid + 1

                                    gameoutput = '<a href="%s#mktsubgrp-caption-%s" target="sky">%s %s   (%s - %s %s)</a>' % (gamelink,dclink,hdwstring,gamewrite,fix,fixdet[0],fixdet[2])
                                    #print gameoutput

                                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/2Goals.html" , 'a')
                                    logfile.write(gameoutput)
                                    logfile.write('<p>')
                                    logfile.close()
                                    break

                                #print doublechance
                                hdw = hdw + 1
                                if hdw == 2:
                                    hdwstring = "[A]"
                                    team2back = fixteams[1]
                                if hdw == 3:
                                    t = 0
                                    hdw = 1
                                    break
                        break
    #Reset the counter
    elif test.find('class="all-bets-toggle"') != -1 and singleBet == 1:
        singleBet = 0
        
if __name__ == "__main__":
    rightnow = datetime.datetime.now().strftime("%d-%m-%y")
    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/2Goals.html" , 'w')
    logfile.write("Odds taken from Sky Bet To Score 2+ Goals on %s %s<br>" % (today.capitalize(),rightnow))
    logfile.write("Using 30/100 - 1/3 - 2/5 - 2/9 - 1/4 - 2/7 - 4/11<br>")
    logfile.write("[H]ome - [A]way<br>")
    #logfile.write('Remember to enter the games on to the site <a href="https://sites.google.com/site/smoggybets/home/weekly-betting-2014-2015" target=smoggybets>here</a><br>')
    logfile.write("---------------------------------------------------------------------------------------------------------------------<br>")
    logfile.write('<br>')
    logfile.close()


    import urllib
    #Reads the web page for Todays Matches
    for w in range (1, 6, 1):
        if w == 1:
            day = today
        elif w == 2:
            day = day2
        elif w == 3:
            day = day3
        elif w == 4:
            day = day4
        elif w == 5:
            day = day5
    
        print ""
        future = now + datetime.timedelta(days=w - 1)
        future = future.strftime("%d-%m-%y")
        print day,future
        print ""

        logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/2Goals.html" , 'a')
        logfile.write('<br>')
        logfile.write('<br>')
        logfile.write("<b><u>" + day.capitalize() + " " + future + "</u></b>")
        #logfile.write(" ")
        #logfile.write(future + "</u>")
        #logfile.write("<br>*******")
        logfile.write('<p>')
        logfile.close()
        
        sock = urllib.urlopen("https://www.skybet.com/football/ev_time/all?p=1&dp=%s" % day)
        htmlSource = sock.read()
        sock.close()

        #Check to see if the page is valid and then continue:
        #if htmlSource.find('<html') != -1:
        xit = 2
        if xit != 1 :
            logfile = open("temp.log", 'w') #This adds to a file to read easier
            logfile.write(htmlSource)
            logfile.close()
            #Read line by line adding one each time
            f = open ("temp.log", "rb")
            multipage = 0
            for j in range (1, 20000, 1):
                test = f.readline()
                if test.find('<li class="total-pages">Page') != -1:
                    #print "multipage"
                    multipage = test
                    multipage = multipage.strip()
                    multipage = multipage[35:]
                    multipage = multipage[:-5]
                    multipage = multipage.strip()
                    multipage = int(multipage)
                    #print multipage
                getData()

            if multipage > 0:
                for p in range (2, multipage + 1, 1):
                    print "Scanning Page: %d for %s" % (p,day)
                    sock = urllib.urlopen("https://www.skybet.com/football/ev_time/all?p=%s&dp=%s" % (p,day))
                    htmlSource = sock.read()
                    sock.close()

                    xit = 2
                    if xit != 1 :
                        logfile = open("temp.log", 'w') #This adds to a file to read easier
                        logfile.write(htmlSource)
                        logfile.close()
            #Read line by line adding one each time
                        f = open ("temp.log", "rb")
                        for j in range (1, 20000, 1):
                            test = f.readline()
                            getData()

                    
            
            print "Games for",day,gamesValid

            logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/2Goals.html" , 'a')
            logfile.write('<br>')
            logfile.write('<br>')
            logfile.write("<b>Games for " + day.capitalize() + ": " + str(gamesValid) + "</b>")
            logfile.write('<br>')
            logfile.write('<hr>')
            logfile.write('<br>')
            logfile.close()
            
            totalValid = totalValid + gamesValid
            gamesValid = 0
            f.close()
    

    print "--------"
    print ""
    print "Games Scanned:",gamesTotal
    print "Games to back:",totalValid

    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/2Goals.html" , 'a')
    logfile.write('<br>')
    logfile.write("<b>" + str(totalValid) + " games to back from " + str(gamesTotal) + " games scanned </b>")
    logfile.write('<br>')
    #logfile.write('Remember to enter the games on to the site <a href="https://sites.google.com/site/smoggybets/home/weekly-betting-2014-2015" target=smoggybets>here</a><br>')
    logfile.close()

