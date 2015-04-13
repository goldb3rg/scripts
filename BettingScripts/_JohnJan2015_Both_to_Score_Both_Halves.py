from sgmllib import SGMLParser
import string
import datetime
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


#As they have changed it! I now need to read the page with all players
#Then write to a single file and not individual ones as before

if __name__ == "__main__":
    rightnow = datetime.datetime.now().strftime("%d-%m-%y")
    logfile = open("John_2015.html" , 'w')
    logfile.write("Odds taken from Sky Bet (in 90 mins) for Games on %s %s<br>" % (today.capitalize(),rightnow))
    logfile.write("Using odds 16/1, 18/1, 20/1 or 22/1 for both teams to score in both halves.<br>")
    logfile.write("---------------------------------------------------------------------------------------------------------------------<br>")
    logfile.write('<br>')
    logfile.close()

    gamesTotal = 0
    gamesValid = 0
    totalValid = 0

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

        logfile = open("John_2015.html" , 'a')
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
            for j in range (1, 100000, 1):
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
    
                if test.find('class="all-bets-toggle"') != -1:
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
                            for k in range (1, 100000, 1):
                                test1 = g.readline()
                                #print test1

                                #get fixture details
                                if test1.find('data-event-headline') != -1:
                                    test1 = g.readline()
                                    fix = test1.strip()
                                    fix = fix[1:]
                                    fix = fix[:-5]

                                if test1.find('<h2 class="event-title sub-head">') != -1:
                                    test1 = g.readline()
                                    test1 = g.readline()
                                    fixdet = test1.strip()
                                    fixdet = fixdet.split('|')
                                    #print fixdet[0]
                                    #print fixdet[2]
                                                                    
                                #get shortcut if it is a Handicap -1 game in prep.
                                if test1.find('id="mktsubgrp-caption-') != -1:
                                    dc = test1.split('"')
                                                                        
                                if test1.find(' Both Teams To Score In Both Halves ') != -1:
                                    dclink = "mktsubgrp-caption-" + dc[3]
                                    print ("dc link: "+ dclink)
                                    t = 1
                                    hdw = 1
                                    hdwstring = "[Yes]"
                                    while t == 1:
                                        test1 = g.readline()
                                        if test1.find('"nofollow"') != -1:
                                            test1 = test1.strip()
                                                #odds
                                            gamesTotal = gamesTotal + 1 
                                            if (test1.find('data-oc-price-num="16" data-oc-price-den="1"') != -1) \
                                            or (test1.find('data-oc-price-num="18" data-oc-price-den="1"') != -1) \
                                            or (test1.find('data-oc-price-num="20" data-oc-price-den="1"') != -1) \
                                            or (test1.find('data-oc-price-num="22" data-oc-price-den="1"') != -1):
                                                #print test
                                                #print test1

                                                gamehyper = test.split('"')
                                                gamedata = test1.split('"')
                                                print gamehyper[3]

                                                gamelink = "http://www.skybet.com" + gamehyper[3]
                                                gamelink = gamelink.strip()
                                                

                                                #print gamedata[7]
                                                #print gamedata[9]
                                                #print gamedata[15]

                                                #print gamedata[15],gamedata[7],"/",gamedata[9]
                                                #print gamelink
                                                gamewrite = gamedata[7] + "/" + gamedata[9]

                                                print gamewrite
                                                print gamelink
                                                print "---------"

                                                league = gamelink.split('/')
                                                #print league[4]
                                                gamesValid = gamesValid + 1

                                                gameoutput = '<a href="%s#%s" target="sky">%s %s   (%s - %s %s)</a>' % (gamelink,dclink,hdwstring,gamewrite,fix,fixdet[0],fixdet[2])
                                                print gameoutput

                                                logfile = open("John_2015.html" , 'a')
                                                logfile.write(gameoutput)
                                                logfile.write('<p>')
                                                logfile.close()
                                
                                            #print doublechance
                                            hdw = hdw + 1
                                            if hdw == 2:
                                                break
                                    break

            if multipage > 0:
                for p in range (2, multipage + 1, 1):
                    #print "Scanning Page: %d for %s" % (p,day)
                    sock = urllib.urlopen("https://www.skybet.com/football/ev_time/all?p=%s&dp=%s" % (p,day))
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
                        for j in range (1, 100000, 1):
                            test = f.readline()
                
                            if test.find('class="all-bets-toggle"') != -1:
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
                                        for k in range (1, 100000, 1):
                                            test1 = g.readline()

                                            #get fixture details
                                            if test1.find('data-event-headline') != -1:
                                                test1 = g.readline()
                                                fix = test1.strip()
                                                fix = fix[1:]
                                                fix = fix[:-5]

                                            if test1.find('<h2 class="event-title sub-head">') != -1:
                                                test1 = g.readline()
                                                test1 = g.readline()
                                                fixdet = test1.strip()
                                                fixdet = fixdet.split('|')
                                                #print fixdet[0]
                                                #print fixdet[2]

                                            #get shortcut if it is a Handicap -1 game in prep.
                                            if test1.find('id="mktsubgrp-caption-') != -1:
                                                dc = test1.split('"')
                                            if test1.find(' Both Teams To Score In Both Halves ') != -1:
                                                dclink = dc[3]
                                                t = 1
                                                hdw = 1
                                                hdwstring = "[Yes]"
                                                while t == 1:
                                                    test1 = g.readline()
                                                    if test1.find('"nofollow"') != -1:
                                                        test1 = test1.strip()
                                                        #Odds
                                                        gamesTotal = gamesTotal + 1 
                                                        if (test1.find('data-oc-price-num="16" data-oc-price-den="1"') != -1) \
                                                        or (test1.find('data-oc-price-num="18" data-oc-price-den="1"') != -1) \
                                                        or (test1.find('data-oc-price-num="20" data-oc-price-den="1"') != -1) \
                                                        or (test1.find('data-oc-price-num="22" data-oc-price-den="1"') != -1):
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
                                                            gamewrite = gamedata[7] + "/" + gamedata[9]

                                                            print gamewrite
                                                            print gamelink
                                                            
                                                            print "---------"
                                                            league = gamelink.split('/')
                                                            #print league[4]
                                                            gamesValid = gamesValid + 1

                                                            gameoutput = '<a href="%s#%s" target="sky">%s %s   (%s - %s %s)</a>' % (gamelink,dclink,hdwstring,gamewrite,fix,fixdet[0],fixdet[2])
                                                            #print gameoutput

                                                            logfile = open("John_2015.html" , 'a')
                                                            logfile.write(gameoutput)
                                                            logfile.write('<p>')
                                                            logfile.close()
                                
                                                        #print doublechance
                                                        hdw = hdw + 1
                                                        if hdw == 2:
                                                            break
                                                break
            
            print "Games for",day,gamesValid

            logfile = open("John_2015.html" , 'a')
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

    logfile = open("John_2015.html" , 'a')
    logfile.write('<br>')
    logfile.write("<b>" + str(totalValid) + " games to back from " + str(gamesTotal) + " games scanned </b>")
    logfile.write('<br>')
    logfile.close()
    
    
    
        
