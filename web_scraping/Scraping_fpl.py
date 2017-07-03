import urllib
from urllib2 import urlopen
from bs4 import BeautifulSoup
import csv
url = 'https://fantasy.premierleague.com/player-list/' 
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
set_of_all_tr_record = soup.findAll('tr')
csvfile = 'fpl.csv'
with open(csvfile, "w") as output:
	writer = csv.writer(output, lineterminator = '\n')
	for record in set_of_all_tr_record:
		some_list = record.findAll('td')
		new_list = list(some_list)
		#print new_list
		list_to_be_written = []
		if len(new_list) != 0:
			#lst[0] = lst[0].encode('ascii', 'ignore').decode('ascii')
			for x in new_list:
				var1 = x.contents
				var1= var1[0].encode('utf-8')
				list_to_be_written.append(var1)
			#print list_to_be_written	
			writer.writerow(list_to_be_written)
			

			"""player = new_list[0].contents
			team = new_list[1].contents
			point = new_list[2].contents
			cost = new_list[3].contents

			player = player[0].encode('utf-8')
			team = team[0].encode('utf-8')
			point = point[0].encode('utf-8')
			cost = cost[0].encode('utf-8')
			list_to_be_written = [player,team,point,cost]
			#print list_to_be_written 
			#print player,team,point,cost
			writer.writerow(list_to_be_written)"""
