from sgmllib import SGMLParser
import string

#As they have changed it! I now need to read the page with all players
#Then write to a single file and not individual ones as before

if __name__ == "__main__":
    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/whopper_suggested.txt" , 'w')
    logfile.write('**********************************************************************')
    logfile.write('\n')
    logfile.write("Suggested Games to bet on with odds 2/9 1/5 2/11 & 1/6")
    logfile.write('\n')
    logfile.write('**********************************************************************')
    logfile.write('\n')
    logfile.close()

    #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/whopper_suggested.txt" , 'w')
    #logfile.write('**********************************************************************')
    #logfile.write('\n')
    #logfile.write("Suggested Games to bet on with odds 1/4")
    #logfile.write('\n')
    #logfile.write('**********************************************************************')
    #logfile.write('\n')
    #logfile.close()

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
        f = open ("/Users/martinbrown/Desktop/BettingScripts/output/whopper.txt", "rb")
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
                if (odds[2] == " 2/9 ") or (odds[2] == " 1/5 ") or (odds[2] == " 2/11 ") or (odds[2] == " 1/6 "):
                    print "Home Win" + test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/whopper_suggested.txt" , 'a')
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
                    logfile.write("Home Win" + test)
                    logfile.close()
                   
                if (odds[4] == " 2/9 ") or (odds[4] == " 1/5 ") or (odds[4] == " 2/11 ") or (odds[4] == " 1/6 "):
                    tmp = test
                    clubs = test
                    print "Draw" + test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/whopper_suggested.txt" , 'a')
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
                    logfile.write("Draw" + test)
                    logfile.close()

                odds[6] = odds[6][:-1]
                if (odds[6] == " 2/9 ") or (odds[6] == " 1/5 ") or (odds[6] == " 2/11 ") or (odds[6] == " 1/6 "):
                    tmp = test
                    clubs = test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/whopper_suggested.txt" , 'a')
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
                    logfile.write("Away Win" + test)
                    logfile.close()


        #Now for Bet 2 ----------------------------------------------------------------------
        logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/whopper_suggested.txt" , 'a')
        logfile.write('\n')
        logfile.write('\n')
        logfile.write('\n')
        logfile.write('\n')
        logfile.write('**********************************************************************')
        logfile.write('\n')
        logfile.write('\n')
        logfile.write("Suggested Games to bet on with odds 1/4")
        logfile.write('\n')
        logfile.write('\n')
        logfile.write('**********************************************************************')
        logfile.write('\n')
        logfile.write('\n')
        logfile.close()

        f = open ("/Users/martinbrown/Desktop/BettingScripts/output/whopper.txt", "rb")
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
                if odds[2] == " 1/4 ":
                    print "Home Win" + test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/whopper_suggested.txt" , 'a')
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
                    logfile.write("Home Win" + test)
                    logfile.close()
                    
                if odds[4] == " 1/4 ":
                    tmp = test
                    clubs = test
                    print "Draw" + test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/whopper_suggested.txt" , 'a')
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
                    logfile.write("Draw" + test)
                    logfile.close()


                odds[6] = odds[6][:-1]
                if odds[6] == " 1/4":
                    tmp = test
                    clubs = test
                    #print "Away Win - " & test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/whopper_suggested.txt" , 'a')
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
                    logfile.write("Away Win" + test)
                    logfile.close()


                #Now write to the XML file
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/uk_suggested.txt" , 'a')
                #logfile.write('\n')
                #logfile.write('\n** ')
                #logfile.write(clubs)
                #logfile.write('\n   --------------------')
                #logfile.close()
        f.close()
