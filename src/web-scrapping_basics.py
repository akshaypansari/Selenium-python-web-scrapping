from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://vahan.parivahan.gov.in/vahan4dashboard/vahan/vahan/view/reportview.xhtml")

print(driver.title) # give title for the page

print(driver.current_url)
print(driver.page_source) # return HTML code for the page

time.sleep(5000)

## conditional commands
#is_displayed()
#is_enabled()
# is_selected

## history navigation
# driver.forward()
#driver.back()
# find elements by xpath  and press click ()
# driver.close() # close the current tab so the cliked tab will keep on working

driver.quit() # close all the browser
