from sgmllib import SGMLParser
import string

#As they have changed it! I now need to read the page with all players
#Then write to a single file and not individual ones as before

if __name__ == "__main__":
    logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'w')
    logfile.write("Odds taken from Sky Bet - Handicap List.")
    logfile.close()

    import urllib
    #Reads the web page for Fridays Matches
    sock = urllib.urlopen("http://www.skybet.com/football/betType/handicap-betting?dp=friday")
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
            #Gets League ********************************************
            if test.find('<h3 class="section-head l2"') != -1:
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n** ')
                logfile.write(testClub)
                logfile.write('\n   -------------------- \n')
                logfile.close()


#---

            #Need to add Carriage return? ********************************************
            if test.find('<h3 class="section-head"') != -1:
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.close()


#---

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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' |')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                #logfile.write(' ')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n\n\n')
                logfile.write("\n-------------------------\n")
                logfile.write(testClub)
                logfile.write("\n-------------------------\n")
                logfile.close()
        f.close()

    #Reads the web page for Saturdays Matches
    sock = urllib.urlopen("http://www.skybet.com/football/betType/handicap-betting?dp=saturday")
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
            #Gets League ********************************************
            if test.find('<h3 class="section-head l2"') != -1:
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n** ')
                logfile.write(testClub)
                logfile.write('\n   -------------------- \n')
                logfile.close()


#---

            #Need to add Carriage return? ********************************************
            if test.find('<h3 class="section-head"') != -1:
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.close()


#---

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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' |')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                #logfile.write(' ')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n\n\n')
                logfile.write("\n-------------------------\n")
                logfile.write(testClub)
                logfile.write("\n-------------------------\n")
                logfile.close()
        f.close()

    #Reads the web page for Saturdays Matches Page 2
    sock = urllib.urlopen("http://www.skybet.com/football/betType/handicap-betting?p=2&dp=saturday")
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
            #Gets League ********************************************
            if test.find('<h3 class="section-head l2"') != -1:
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n** ')
                logfile.write(testClub)
                logfile.write('\n   -------------------- \n')
                logfile.close()


#---

            #Need to add Carriage return? ********************************************
            if test.find('<h3 class="section-head"') != -1:
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.close()


#---

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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' |')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                #logfile.write(' ')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' | ')
                logfile.close()
        f.close()

   #Reads the web page for Saturdays Matches Page 3
    sock = urllib.urlopen("http://www.skybet.com/football/betType/handicap-betting?p=3&dp=saturday")
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
            #Gets League ********************************************
            if test.find('<h3 class="section-head l2"') != -1:
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n** ')
                logfile.write(testClub)
                logfile.write('\n   -------------------- \n')
                logfile.close()


#---

            #Need to add Carriage return? ********************************************
            if test.find('<h3 class="section-head"') != -1:
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.close()


#---

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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' |')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                #logfile.write(' ')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' | ')
                logfile.close()
        f.close()

   #Reads the web page for Saturdays Matches page 4
    sock = urllib.urlopen("http://www.skybet.com/football/betType/handicap-betting?p=4&dp=saturday")
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
            #Gets League ********************************************
            if test.find('<h3 class="section-head l2"') != -1:
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n** ')
                logfile.write(testClub)
                logfile.write('\n   -------------------- \n')
                logfile.close()


#---

            #Need to add Carriage return? ********************************************
            if test.find('<h3 class="section-head"') != -1:
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.close()


#---

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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' |')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                #logfile.write(' ')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' | ')
                logfile.close()
        f.close()

   #Reads the web page for Saturdays Matches Page 5
    sock = urllib.urlopen("http://www.skybet.com/football/betType/handicap-betting?p=5&dp=saturday")
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
            #Gets League ********************************************
            if test.find('<h3 class="section-head l2"') != -1:
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n** ')
                logfile.write(testClub)
                logfile.write('\n   -------------------- \n')
                logfile.close()


#---

            #Need to add Carriage return? ********************************************
            if test.find('<h3 class="section-head"') != -1:
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.close()


#---

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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' |')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                #logfile.write(' ')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' | ')
                logfile.close()
        f.close()


    #Reads the web page for Sundays Matches
    sock = urllib.urlopen("http://www.skybet.com/football/betType/handicap-betting?dp=sunday")
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
            #Gets League ********************************************
            if test.find('<h3 class="section-head l2"') != -1:
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n** ')
                logfile.write(testClub)
                logfile.write('\n   -------------------- \n')
                logfile.close()


#---

            #Need to add Carriage return? ********************************************
            if test.find('<h3 class="section-head"') != -1:
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.close()


#---

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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' |')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                #logfile.write(' ')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n\n\n')
                logfile.write("\n-------------------------\n")
                logfile.write(testClub)
                logfile.write("\n-------------------------\n")
                logfile.close()
        f.close()

    #Reads the web page for Saturdays Matches
    sock = urllib.urlopen("http://www.skybet.com/football/betType/handicap-betting?dp=monday")
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
            #Gets League ********************************************
            if test.find('<h3 class="section-head l2"') != -1:
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n** ')
                logfile.write(testClub)
                logfile.write('\n   -------------------- \n')
                logfile.close()


#---

            #Need to add Carriage return? ********************************************
            if test.find('<h3 class="section-head"') != -1:
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.close()


#---

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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n')
                logfile.write('\n')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' |')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                #logfile.write(' ')
                logfile.write(' ~ ')
                logfile.write(testClub)
                #logfile.write(' | ')
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
                logfile = open("/Users/martinbrown/Desktop/BettingScripts/output/handicap.txt" , 'a')
                logfile.write('\n\n\n')
                logfile.write("\n-------------------------\n")
                logfile.write(testClub)
                logfile.write("\n-------------------------\n")
                logfile.close()
        f.close()


