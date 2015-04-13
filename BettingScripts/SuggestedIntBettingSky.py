from sgmllib import SGMLParser
import string

#As they have changed it! I now need to read the page with all players
#Then write to a single file and not individual ones as before

if __name__ == "__main__":
    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_suggested.txt" , 'w')
    logfile.write('**********************************************************************')
    logfile.write('\n')
    logfile.write("Suggested International Games to bet on for Bet 1 with odds 30/100 1/3 2/5 2/9 1/4 2/7 4/11")
    logfile.write('\n')
    logfile.write('**********************************************************************')
    logfile.write('\n')
    logfile.close()

    import urllib
    #Reads the web page for the GK players info
    #sock = urllib.urlopen("http://www.skybet.com/football/coupon/uk-long-list")
    #htmlSource = sock.read()
    #sock.close()

    #Check to see if the page is valid and then continue:
    #if htmlSource.find('<html') != -1:
    xit = 2
    if xit != 1 :
        #logfile = open("temp.log", 'w') #This adds to a file to read easier
        #logfile.write(htmlSource)
        #logfile.close()
        #Read line by line adding one each time
        f = open ("/Users/martinbrown/Desktop/BettingScripts/output/int_odds.txt", "rb")
        for j in range (1, 10000, 1):
            test = f.readline()
            odds = test.split("-")

            #Get Date
            if test.find('2013') != -1 or test.find('2014') != -1:
                kickoff = test
                kickwrote = 0
                leaguewrote = 0
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/uk_suggested.txt" , 'a')
                #logfile.write('\n')
                #logfile.write('----------------------------------------------------------------------')
                #logfile.write('\n')
                #logfile.write(test)
                #logfile.write('----------------------------------------------------------------------')
                #logfile.write('\n')
                #logfile.close()
            
            #find league type and write
            if test.find('**') != -1:
                league = test
                leaguewrote = 0
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/uk_suggested.txt" , 'a')
                #logfile.write('\n')
                #logfile.write(test)
                #logfile.close()

            if len(odds) == 7 :
                #print odds
                #Gets Bet 1
                if (odds[2] == " 30/100 ") or (odds[2] == " 1/3 ") or (odds[2] == " 2/5 ") or (odds[2] == " 2/9 ") or (odds[2] == " 1/4 ") or (odds[2] == " 2/7 ") or (odds[2] == " 4/11 "):
                    print "Home Win - " + test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_suggested.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    if leaguewrote == 0:                       
                        logfile.write('\n')
                        logfile.write(league)
                        leaguewrote = 1
                    logfile.write('\n')
                    logfile.write("Home Win - " + test)
                    logfile.close()
                   
                if (odds[4] == " 30/100 ") or (odds[4] == " 1/3 ") or (odds[4] == " 2/5 ") or (odds[4] == " 2/9 ") or (odds[4] == " 1/4 ") or (odds[4] == " 2/7 ") or (odds[4] == " 4/11 "):
                    tmp = test
                    clubs = test
                    print "Draw - " & test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_suggested.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    if leaguewrote == 0:                       
                        logfile.write('\n')
                        logfile.write(league)
                        leaguewrote = 1
                    logfile.write('\n')
                    logfile.write("Draw - " + test)
                    logfile.close()

                odds[6] = odds[6][:-1]
                if (odds[6] == " 30/100") or (odds[6] == " 1/3") or (odds[6] == " 2/5") or (odds[6] == " 2/9") or (odds[6] == " 1/4")  or (odds[6] == " 2/7") or (odds[6] == " 4/11"):
                    tmp = test
                    clubs = test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_suggested.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    if leaguewrote == 0:                       
                        logfile.write('\n')
                        logfile.write(league)
                        leaguewrote = 1
                    logfile.write('\n')
                    logfile.write("Away Win - " + test)
                    logfile.close()


        #Now for Bet 2 ----------------------------------------------------------------------
        logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_suggested.txt" , 'a')
        logfile.write('\n')
        logfile.write('\n')
        logfile.write('\n')
        logfile.write('\n')
        logfile.write('**********************************************************************')
        logfile.write('\n')
        logfile.write('\n')
        logfile.write("Suggested International Games to bet on for Bet 2 with odds 8/11 3/4 4/5 5/6 10/11 19/20 20/21")
        logfile.write('\n')
        logfile.write('\n')
        logfile.write('**********************************************************************')
        logfile.write('\n')
        logfile.write('\n')
        logfile.close()

        f = open ("/Users/martinbrown/Desktop/BettingScripts/output/int_odds.txt", "rb")
        for j in range (1, 10000, 1):
            test = f.readline()
            odds = test.split("-")

            #Get Date
            if test.find('2013') != -1 or test.find('2014') != -1:
                kickoff = test
                kickwrote = 0
                leaguewrote = 0
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/uk_suggested.txt" , 'a')
                #logfile.write('\n')
                #logfile.write('----------------------------------------------------------------------')
                #logfile.write('\n')
                #logfile.write(test)
                #logfile.write('----------------------------------------------------------------------')
                #logfile.write('\n')
                #logfile.close()
                
            #find league type and write
            if test.find('**') != -1:
                league = test
                leaguewrote = 0
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/uk_suggested.txt" , 'a')
                #logfile.write('\n')
                #logfile.write(test)
                #logfile.close()
                
            if len(odds) == 7 :
                #print odds
                #Gets Bet 1
                if (odds[2] == " 3/4 ") or (odds[2] == " 4/5 ") or (odds[2] == " 5/6 ") or (odds[2] == " 10/11 ") or (odds[2] == " 20/21 ") or (odds[2] == " 8/11 ") or (odds[2] == " 19/20 "):
                    print "Home Win - " + test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_suggested.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    if leaguewrote == 0:                       
                        logfile.write('\n')
                        logfile.write(league)
                        leaguewrote = 1
                    logfile.write('\n')
                    logfile.write("Home Win - " + test)
                    logfile.close()
                    
                if (odds[4] == " 3/4 ") or (odds[4] == " 4/5 ") or (odds[4] == " 5/6 ") or (odds[4] == " 10/11 ") or (odds[4] == " 20/21 ") or (odds[4] == " 8/11 ") or (odds[4] == " 19/20 "):
                    tmp = test
                    clubs = test
                    print "Draw - " & test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_suggested.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    if leaguewrote == 0:                       
                        logfile.write('\n')
                        logfile.write(league)
                        leaguewrote = 1
                    logfile.write('\n')
                    logfile.write("Draw - " + test)
                    logfile.close()


                odds[6] = odds[6][:-1]
                if (odds[6] == " 3/4") or (odds[6] == " 4/5") or (odds[6] == " 5/6") or (odds[6] == " 10/11") or (odds[6] == " 20/21") or (odds[6] == " 8/11") or (odds[6] == " 19/20"):
                    tmp = test
                    clubs = test
                    #print "Away Win - " & test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_suggested.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    if leaguewrote == 0:                       
                        logfile.write('\n')
                        logfile.write(league)
                        leaguewrote = 1
                    logfile.write('\n')
                    logfile.write("Away Win - " + test)
                    logfile.close()


                #Now write to the XML file
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/uk_suggested.txt" , 'a')
                #logfile.write('\n')
                #logfile.write('\n** ')
                #logfile.write(clubs)
                #logfile.write('\n   --------------------')
                #logfile.close()
        f.close()
