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
	for link in allLinks[:1]:
		url = link['href']
		print "Trying to fetch " + url

		request = urllib2.Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
		data = urllib2.urlopen(request).read()
		soup2 = Soup(data)
		script =  str(soup2.body.script.contents[0])
		videoiframeEncoded = script.split('"')[-2]
		videoiframeDecoded = urllib2.unquote(videoiframeEncoded)
		soup3 = Soup(videoiframeDecoded)
		videourl = soup3.iframe['src']
		# print videourl
		# print type(videourl)
		request = urllib2.Request(videourl,headers = {'User-Agent': 'Mozilla/5.0'})
		video = urllib2.urlopen(request).read()
		soup4 = Soup(video)
		finalurl =  soup4.video.source
		print finalurl['src']
		request = urllib2.Request(finalurl['src'],headers = {'User-Agent': 'Mozilla/5.0'})
		print "Downloading Video"
		video = urllib2.urlopen(request).read()
		print "Saving Video"
		with open('episode.mp4','wb') as f:
			f.write(video)
		print "Done"

	# i = 0
	# download = False 
	# while i<len(allLinks):
	# 	if not video_to_download in allLinks[i]:
	# 		i += 1
	# 		download = True

	





if __name__ == "__main__":
	main()