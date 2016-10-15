####### webseiten-inhalte crawlen - beautifulsoup #######
#########################################################

import requests
from bs4 import BeautifulSoup

print('geileWelt')
url = "http://jedermenschistzuviel.stabo.org/texte.php"

## zum "weiterblättern":

url_page_2 = url + '&page=' + str(2) + '&s=relevance'

# def get_data_from_url(url, 10): ## wie viele Seiten sollen durchsucht werden?

# r = requests.get("url")
r = requests.get("http://jedermenschistzuviel.stabo.org/texte.php")
r.content

soup = BeautifulSoup(r.content)
print(soup.prettify())

## alle links zwischen </a> tags finden:
## link-texte und absolute links finden:

links = soup.find_all("a")
for link in links:
	#if "http" in link.get("href"): ## gibt die absoluten links
		print("<a href='%s'>%s</a>" %(link.get("href"), link.text))



## weitere informationen crawlen:

g_data = soup.find_all("div") ## ("", {"class": "info"}) für weitere Infos
print(g_data)

for item in g_data:
	print(item.text)
	print(item)
	print(item.contents)
	print(item.contents[0])
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




