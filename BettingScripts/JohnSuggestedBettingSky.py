from sgmllib import SGMLParser
import string

#As they have changed it! I now need to read the page with all players
#Then write to a single file and not individual ones as before

if __name__ == "__main__":
    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'w')
    logfile.write('**********************************************************************')
    logfile.write('\n')
    logfile.write("Suggested Games to bet on with odds 2/9 1/4 2/7")
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
        f = open ("/Users/martinbrown/Desktop/BettingScripts/output/uk_odds.txt", "rb")
        for j in range (1, 10000, 1):
            test = f.readline()
            odds = test.split("-")

            #Get Date
            if test.find('2013') != -1 or test.find('2014') != -1:
                kickoff = test
                kickwrote = 0
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                #logfile.write('\n')
                #logfile.write('----------------------------------------------------------------------')
                #logfile.write('\n')
                #logfile.write(kickoff)
                #logfile.write('----------------------------------------------------------------------')
                #logfile.write('\n')
                #kickwrote = 1
                #logfile.close()
            
            #find league type and write
            if test.find('**') != -1:
                league = test
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                #logfile.write('\n')
                #logfile.write(test)
                #logfile.close()

            if len(odds) == 7 :
                #print odds
                #Gets Bet 1
                if (odds[2] == " 2/9 ") or (odds[2] == " 1/4 ") or (odds[2] == " 2/7 "):
                    print "Home Win - " + test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    logfile.write('\n')
                    logfile.write(league)
                    logfile.write('\n')
                    logfile.write("Home Win" + test)
                    logfile.close()
                   
                if (odds[4] == " 2/9 ") or (odds[4] == " 1/4 ") or (odds[4] == " 2/7 "):
                    tmp = test
                    clubs = test
                    print "Draw - " & test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    logfile.write('\n')
                    logfile.write(league)
                    logfile.write('\n')
                    logfile.write("Draw" + test)
                    logfile.close()

                odds[6] = odds[6][:-1]    
                if (odds[6] == " 2/9") or (odds[6] == " 1/4") or (odds[6] == " 2/7"):
                    tmp = test
                    clubs = test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    logfile.write('\n')
                    logfile.write(league)
                    logfile.write('\n')
                    logfile.write("Away Win" + test)
                    logfile.close()

        f.close()
        
        f = open ("/Users/martinbrown/Desktop/BettingScripts/output/euro_odds.txt", "rb")
        for j in range (1, 10000, 1):
            test = f.readline()
            odds = test.split("-")

            #Get Date
            if test.find('2013') != -1 or test.find('2014') != -1:
                kickoff = test
                kickwrote = 0
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                #logfile.write('\n')
                #logfile.write('----------------------------------------------------------------------')
                #logfile.write('\n')
                #logfile.write(kickoff)
                #logfile.write('----------------------------------------------------------------------')
                #logfile.write('\n')
                #kickwrote = 1
                #logfile.close()
            
            #find league type and write
            if test.find('**') != -1:
                league = test
                #logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                #logfile.write('\n')
                #logfile.write(test)
                #logfile.close()

            if len(odds) == 7 :
                #print odds
                #Gets Bet 1
                if (odds[2] == " 2/9 ") or (odds[2] == " 1/4 ") or (odds[2] == " 2/7 "):
                    print "Home Win - " + test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    logfile.write('\n')
                    logfile.write(league)
                    logfile.write('\n')
                    logfile.write("Home Win" + test)
                    logfile.close()
                   
                if (odds[4] == " 2/9 ") or (odds[4] == " 1/4 ") or (odds[4] == " 2/7 "):
                    tmp = test
                    clubs = test
                    print "Draw - " & test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    logfile.write('\n')
                    logfile.write(league)
                    logfile.write('\n')
                    logfile.write("Draw" + test)
                    logfile.close()

                odds[6] = odds[6][:-1]    
                if (odds[6] == " 2/9") or (odds[6] == " 1/4") or (odds[6] == " 2/7"):
                    tmp = test
                    clubs = test
                    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/johnsbets.txt" , 'a')
                    if kickwrote == 0:
                        logfile.write('\n')
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        logfile.write(kickoff)
                        logfile.write('----------------------------------------------------------------------')
                        logfile.write('\n')
                        kickwrote = 1
                    logfile.write('\n')
                    logfile.write(league)
                    logfile.write('\n')
                    logfile.write("Away Win" + test)
                    logfile.close()

        f.close()
