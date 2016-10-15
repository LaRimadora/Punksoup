####### webseiten-inhalte crawlen - beautifulsoup #######
#########################################################

import re
import requests
from bs4 import BeautifulSoup

print('geileWelt')
#url = "http://jedermenschistzuviel.stabo.org/texte.php"
#url_page_2 = url + '&page=' + str(2) + '&s=relevance'

# r = requests.get("url")
r = requests.get("http://jedermenschistzuviel.stabo.org/texte.php?show=2&what=7357")
r.content

soup = BeautifulSoup(r.content)
#print(soup.prettify())

g_data = soup.find("td", style="border:1px solid #0080ff;text-align:left;vertical-align:top;padding-left:10px;padding-right:7px;")
print(g_data.text)

#i = 0
#for item in g_data:
#	print(i, item.text)
#	i = i + 1

a = re.search('Nazi', g_data.text)
print(a)

#for tag in g_data[6].re.compile("h1"):
#	print(tag)










## alle links zwischen </a> tags finden:
## link-texte und absolute links finden:

#links = soup.find_all("a")
#for link in links:
	#if "http" in link.get("href"): ## gibt die absoluten links
		#print("<a href='%s'>%s</a>" %(link.get("href"), link.text))



## weitere informationen crawlen:

#g_data = soup.find_all("div") ## ("", {"class": "info"}) für weitere Infos
#print(g_data)

#for item in g_data:
	#print(item.text)
	#print(item)
	#print(item.contents)
	#print(item.contents[0])
	#print(item.contents[0].text) ## printet unterclassen [0] von div mit aus
	#print(item.contents[0].find_all("a", {"class": "id"})[0].text)
	
	##print(item.contents[1].find_all("li", {"class": "title"})[0].text)



## Arbeitsschritte ##

#for link in soup.find_all("a"):
#	link.get("href")
	
## strings von Links printen:
	
#for link in soup.find_all("a"):
#	print(link.get("href"))
#	print(link.text)
#	print(link.text, link.get("href") ## link.text und link
	
#for link in soup.find_all("a"):	
 #   "<a href='%s'>%s</a>" %(link.get("href"), link.text)



