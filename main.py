import requests
from bs4 import BeautifulSoup

search = []
skip = 0
print("OpenNet parser v0.2 | all - display all news | y - start\n")

while True:
	searchInput=input("Search Keyword: ")
	if searchInput == 'y':
		break
	elif searchInput == ('all'):
		search = [' ']
		break
	else:
		search.append(searchInput)
			
print("\n     Date     Srh. key.                      Link                                       News                \n")
while True:
	try:
		url = "https://opennet.ru/opennews/index.shtml?skip={}&news=open&template=0".format(str(skip))
		
		page = requests.get(url)
		soup = BeautifulSoup(page.text, 'html.parser')
		dates = soup.find_all('td', class_='tdate')
		news = soup.find_all('a', class_='title2')
		
		for i in range(0 , len(news)): 
			for keyword in search:
				if keyword in news[i].text:	
					print("* "+dates[i].text,end=' ')
					print(keyword.center(10),end=' ')
					print("https://opennet.ru"+news[i].get('href'),end='  ')
					print(news[i].text)
				
		skip += 15
		
	except KeyboardInterrupt:
		break
