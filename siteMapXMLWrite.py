from datetime import datetime
from urllib.parse import quote

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%dT%H:%M:%S%z")
dateFileName = now.strftime("%Y-%m-%dT%H-%M-%S%z")

file1 = open('urls.txt', 'r')
count = 0

saveSiteMapFile = 'sitemap'+dateFileName+'.xml'
fObject = open(saveSiteMapFile, 'a')

xmlHeader = '''<?xml version="1.0" encoding="UTF-8"?>
    <urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
'''

fObject.write(xmlHeader)

while True:
    count += 1
    line = file1.readline()
  
    if not line:
        break
      
    outputUrl = line.strip()
    encoded_url = quote(outputUrl)
    
    xmlUrlAppend = '''
    <url>
      <loc>'''+ encoded_url +'''</loc>
      <lastmod>'''+formatted_date+'''</lastmod>
    </url>
    '''
    
    fObject.write(xmlUrlAppend)
    
    print("URL {}: {}".format(count, outputUrl))
  
file1.close()

xmlFooter = '''
</urlset>
'''

fObject.write(xmlFooter)