from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()

#****************************************ENTER URL IN DRIVER.GET('')*****************************

driver.get('https://www.bestbuy.com/site/evga-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6434198.p?skuId=6434198')
driver.maximize_window()

# This portion will attempt to find and click on the add to cart button of the requested Best Buy URL
# If it does not find one, it refreshes the page after 30 seconds.
while True:
    try:
        driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8]/div[1]/div/div/div/button').click()
        time.sleep(6)
        driver.find_element_by_xpath('/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a').click()
    except NoSuchElementException:
        time.sleep(30)
        driver.refresh()
