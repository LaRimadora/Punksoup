####### webseiten-inhalte crawlen - beautifulsoup #######
#########################################################

import requests
from bs4 import BeautifulSoup

print('geileWelt')

myRequests = requests.get("http://jedermenschistzuviel.stabo.org/texte.php?show=2&what=7357")
myRequests.content

soup = BeautifulSoup( myRequests.content.decode('ISO-8859-1', 'ignore') )
websiteData = soup.html.find_all("td")
textData 	= websiteData[6].find_all_next(text=True)

i = 0
while textData[i] != "zurück zur Bandübersicht":
	print(textData[i])
	i = i+1



# --- TITLE
# newData = g_data[6].find_all("h1", text=True)
# print( newData )







# i = 0
# for item in g_data:
# 	print( item.text )

## alle links zwischen </a> tags finden:
## link-texte und absolute links finden:

# myLinks = soup.find_all("a")
# for link in myLinks:
# 	if "http" in link.get("href"): ## gibt die absoluten links
		# print("<a href='%s'>%s</a>" %(link.get("href"), link.text))



# weitere informationen crawlen:

# g_data = soup.find_all("div") ## ("", {"class": "info"}) fuer weitere Infos
# print(g_data)

# for item in g_data:
# 	print(item.text)
# 	print(item)
# 	print(item.contents)
# 	print(item.contents[0])
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




