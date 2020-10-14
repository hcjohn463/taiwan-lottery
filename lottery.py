from bs4 import BeautifulSoup
from collections import Counter
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

domain = 'http://www.nfd.com.tw/lottery/power-38/'
year = 2008
blackNums = []
redNums = []
while(year <= 2020):
	url = domain + str(year) + '.htm'
	htmlfile = requests.get(url)
	soup = BeautifulSoup(htmlfile.text,'lxml')
	tds = soup.find_all('td')
	tmpNums = []
	for td in tds:
		align = td['align']
		height = td['height']
		b = td.find('b')
		if height == '19':
			tmpNums.append(b.text)
	for i in range(len(tmpNums)):
		if 3 <= i % 11 <= 8:
			blackNums.append(int(tmpNums[i].strip('\n')))
		if i % 11 == 9:
			redNums.append(int(tmpNums[i].strip('\n')))
	year = year + 1
a = np.array(blackNums)
blackAll = list(np.bincount(a))
a = np.array(redNums)
redAll = list(np.bincount(a))

blackAll = blackAll[1::]
redAll = redAll[1::]

nums = []
for i in range(1,len(blackAll) + 1):
	nums.append(i)
blackDict = dict(zip(nums,blackAll))
print('中獎號出現次數(由少至多):')
print({k: v for k, v in sorted(blackDict.items(), key=lambda item: item[1])})

nums = []
for i in range(1,len(redAll) + 1):
	nums.append(i)
redDict = dict(zip(nums,redAll))
print('特別號出現次數(由少至多):')
print({k: v for k, v in sorted(redDict.items(), key=lambda item: item[1])})