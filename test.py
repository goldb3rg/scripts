import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = selenium.webdriver.Firefox()
driver.get("http://www.skybet.com/football/coupon/all-matches-by-day")
assert "All Matches By Day" in driver.title
elem = driver.find_elements_by_class_name("all-bets-link")

linkstr = ""
for items in elem:
    #print items.text
    linkstr = items.get_attribute('href')
    h = items.find_elements(By.XPATH, '//button')
    print linkstr
    print h

    
assert "No results found." not in driver.page_source
driver.close()

