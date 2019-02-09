from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lxml import etree
browser = webdriver.Chrome()
browser.get("http://dgepb.dg.gov.cn/publicfiles//business/htmlfiles/dgepb/lssq/list.htm")
local_page = browser.find_element_by_id("CP8")
page_num = int(local_page.get_attribute("value"))
print(page_num)
while page_num < 6:
    page = etree.HTML(browser.page_source)
    elem = browser.find_element_by_xpath('//*[@id="mytab11"]/tbody/tr/td/table/tbody/tr/td[5]/a').click()
    print(browser.page_source)


browser.close()