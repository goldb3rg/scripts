from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.skybet.com/football/coupon/all-matches-by-day")
assert "All Matches By Day" in driver.title
elem = driver.find_elements_by_class_name("all-bets-link")

for items in elem:
    print items.text

assert "No results found." not in driver.page_source
driver.close()