from bs4 import BeautifulSoup as Soup
import urllib2
import time


video_to_download = ""
with open('last_downloaded.txt','r') as f:
	last_episode = f.read()
	video_to_download = int(last_episode)+1
number_of_videos = raw_input('How many videos to download? Type 0 for all upto recent.\n')
number_of_videosC = number_of_videos

def download(item):
	global number_of_videosC
	global number_of_videos
	if number_of_videosC == "0":
		return True
	else:
		return int(number_of_videos)

def main():

	global number_of_videosC
	global number_of_videos

	global video_to_download
	url = "http://www.onepiece.tv/"
	request = urllib2.Request(url,headers = {'User-Agent': 'Mozilla/5.0'})

	data = urllib2.urlopen(request).read()

	soup = Soup(data)
	body = soup.body

	allLinks = body.findAll('a',attrs = {'class':'movie'})
	#allLinks = tableofepisodes.findAll('a')
	lastUploadedUrl = allLinks[0]
	lastVideo = int(lastUploadedUrl['href'].split('-')[3])
	while video_to_download <=lastVideo and download(number_of_videos):
		print "Updating your episode library"
		url = "http://www1.watchop.com/watch/one-piece-episode-"+str(video_to_download)+"-english-subbed/"
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
		with open('Onepiece-'+str(video_to_download)+'.mp4','wb') as f:
			f.write(video)
		print "Done"
		number_of_videos = str(int(number_of_videos) -1)
		video_to_download += 1
		with open('last_downloaded.txt','w') as f:
			f.write(str(video_to_download))
		time.sleep(5)

	# i = 0
	# download = False 
	# while i<len(allLinks):
	# 	if not video_to_download in allLinks[i]:
	# 		i += 1
	# 		download = True

	





if __name__ == "__main__":
	main()