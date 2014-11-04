from bs4 import BeautifulSoup as Soup
import urllib2



# with open('last_downloaded.txt','r') as f:
# 	last_episode = f.read()
# 	video_to_download = str(int(last_episode)+1)


def main():
	url = "http://www.onepiece.tv/"
	request = urllib2.Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
#	request.add_header('User-Agent' : 'Mozilla/5.0')
	data = urllib2.urlopen(request).read()

	soup = Soup(data)
	body = soup.body

	allLinks = body.findAll('a',attrs = {'class':'movie'})
	#allLinks = tableofepisodes.findAll('a')
	for link in allLinks:
		url = link['href']
		print "Downloading " + url

		request = urllib2.Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
		data = urllib2.urlopen(request).read()
		print "Saving Video"
		with open('Episode.mp4','wb') as f:
			f.write(data)

	# i = 0
	# download = False 
	# while i<len(allLinks):
	# 	if not video_to_download in allLinks[i]:
	# 		i += 1
	# 		download = True

	





if __name__ == "__main__":
	main()