from selenium import webdriver
from bs4 import BeautifulSoup
import re

domain = 'angular.io'
url = 'https://www.angular.io/'
extractFilename = 'urls.txt'
normalizeUrlStringSearch = 'https://'

driver = webdriver.Firefox()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
fObject = open(extractFilename, 'a')

for link in soup.find_all('a'):
    extractedUrl = str(link.get('href')) + '\n'
    rgx = re.search("^https://", extractedUrl)
    
    # Normalize links if relative path
    if rgx:
        apString = ""
        normalizeUrls =  extractedUrl
    else:
        apString = normalizeUrlStringSearch
        normalizeUrls = apString + domain + extractedUrl
    
    print(normalizeUrls)
    fObject.write(normalizeUrls)
    
driver.quit()