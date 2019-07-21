import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint
import sys
import datetime

if len(sys.argv) < 6:
	print('Less arguments provided')
	print('5 arguments needed => source_stn_code dest_stn_code travel_date travel_month travel_year')
	sys.exit()

source_stn = sys.argv[1]
dest_stn = sys.argv[2]
date = sys.argv[3]
month = sys.argv[4]
year = sys.argv[5]

try:
	datetime.datetime(int(year), int(month), int(date))
except:
	print('The date you entered is not valid')
	sys.exit()

url = 'https://www.railyatri.in/booking/trains-between-stations?from_code='+source_stn+'&from_name=SRC+&journey_date='+date+'%2F'+month+'%2F'+year+'%2F'+'&to_code='+dest_stn+'&to_name=DST+&user_id=1&user_token=6'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
trains = []
for row in soup.select('tr.tbs-main-row'):
	data = {}
	title = row.find('p', {'class': 'train-name-title'}).text.strip('\n')
	data['trn_no'] = title[:5]
	data['trn_name'] = title[8:]
	data['schedule'] = 'https://erail.in/train-enquiry/'+title[:5]
	spans = row.find_all('span')[:6]
	data['source'] = spans[0].text
	data['departure time'] = spans[1].text
	data['destination'] = spans[3].text
	data['arrival time'] = spans[4].text
	data['duration'] = spans[5].text
	data['fares'] = []
	classes = row.find_all('div', {'class': 'coach'})
	for i in range(len(classes)//2):
		pair = {}
		deets = classes[i].find_all('p')
		pair['Class'] = deets[0].text
		pair['Price'] = deets[1].text
		if pair['Price'] == '₹ NA':
			continue
		data['fares'].append(pair)
	if len(data['fares']) != 0:		#railyatri shows some trains with no availabilities
		trains.append(data)

pprint(trains)
