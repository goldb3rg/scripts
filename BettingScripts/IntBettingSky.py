from sgmllib import SGMLParser
import string

#As they have changed it! I now need to read the page with all players
#Then write to a single file and not individual ones as before

if __name__ == "__main__":
    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_odds.txt" , 'w')
    logfile.write("Odds taken from Sky Bet - European Elite List")
    logfile.close()

    import urllib
    #Reads the web page for the GK players info
    sock = urllib.urlopen("http://www.skybet.com/football/coupon/international-list")
    htmlSource = sock.read()
    sock.close()

    #Check to see if the page is valid and then continue:
    #if htmlSource.find('<html') != -1:
    xit = 2
    if xit != 1 :
        logfile = open("eutemp.log", 'w') #This adds to a file to read easier
        logfile.write(htmlSource)
        logfile.close()
        #Read line by line adding one each time
        f = open ("eutemp.log", "rb")
        for j in range (1, 10000, 1):
            test = f.readline()
            #Gets League ********************************************
            if test.find('<h3 class="section-head"') != -1:
                tmp = test
                tmp = tmp.strip() #clears whitespace
                tmp = tmp.strip('</h3>')
                testClub = f.readline()
                testClub = testClub.strip()
                testClub = testClub.strip('</h3>')
                clubs = testClub
                #testClub = testClub.split(' ')

                
                print clubs

                #Now write to the XML file
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_odds.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n** ')
                logfile.write(testClub)
                logfile.write('\n   --------------------')
                logfile.close()

            #Gets Kick Off Time ************************************
            if test.find('<td class="tc1">') != -1:
                tmp = test
                tmp = tmp.strip() #clears whitespace
                tmp = tmp.strip('</td>')
                testClub = tmp
                testClub = testClub.strip()
                testClub = testClub[12:]
                clubs = testClub
                #testClub = testClub.split(' ')

                print clubs

                #Now write to the XML file
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_odds.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n')
                logfile.write(testClub)
                #logfile.write(' - ')
                logfile.close()

            #Gets Team  *******************************************
            if test.find('<span class="oc-desc">') != -1:
                tmp = test
                tmp = tmp.strip() #clears whitespace
                #tmp = tmp.strip('</span>')
                testClub = tmp
                testClub = testClub.strip()
                testClub = testClub[22:]
                testClub = testClub[:-7]
                clubs = testClub

                print clubs

                #Now write to the XML file
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_odds.txt" , 'a')
                logfile.write(' - ')
                logfile.write(testClub)
                #logfile.write(' -')
                logfile.close()

            #Gets Odds *********************************************
            if test.find('<b class="odds">') != -1:
                tmp = test
                tmp = tmp.strip() #clears whitespace
                tmp = tmp.strip('</b>')
                testClub = tmp
                testClub = testClub.strip()
                testClub = testClub[13:]
                #testClub = testClub[:-7]
                clubs = testClub

                print clubs

                #Now write to the XML file
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_odds.txt" , 'a')
                #logfile.write(' ')
                logfile.write(' - ')
                logfile.write(testClub)
                #logfile.write(' - ')
                logfile.close()

            #Gets Date *********************************    
            if test.find('<h2 >') != -1:
                tmp = test
                tmp = tmp.strip() #clears whitespace
                tmp = tmp.strip('</h2>')
                tmp = tmp.strip('</h2>')
                testClub = tmp
                testClub = testClub.strip()
                testClub = testClub.strip('<h2 >')
                #testClub = testClub[28:]
                testClub = testClub.strip('</h2>')

                print testClub

                #Now write to the XML file
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/int_odds.txt" , 'a')
                logfile.write('\n\n\n')
                logfile.write("\n-------------------------\n")
                logfile.write(testClub)
                logfile.write("\n-------------------------\n")
                logfile.close()
        f.close()


