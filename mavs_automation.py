import time
from selenium import webdriver

#check the status of the mavericks game

## take input argument 

driver = webdriver.Chrome('/Users/dasay/website_login/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('mavs game')
search_box.submit()
#time.sleep() # Let the user actually see something!
#driver.quit()




