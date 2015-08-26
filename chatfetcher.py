import base64
import json
import time
import urllib.request
import xml.etree.ElementTree as ET
URL_TEMPLATE = "http://www.youtube.com/live_comments?action_get_comments=1" +\
	"&video_id={video_id}&lt={time}&format=json&pd=10000" + \
	"&rc={counter}&scr=true&comment_version=1"

class FetchTube:
	def __init__(self, video_id):
		self.last_time = int(time.time())
		self.rc = 0
		self.video_id = video_id
	def fetch(self):
		"""
		returns: tuple of (comments, poll_delay)
		"""
		rc = self.rc
		self.rc += 1
		if self.rc > 5:
			self.rc = 0
		url = URL_TEMPLATE.format(video_id=self.video_id,
			time = self.last_time,
			counter = rc)
		print(url)
		with urllib.request.urlopen(url) as indata:
			outxml = ET.parse(indata)
		payload = json.loads(outxml.find("html_content").text)
		self.last_time = payload["latest_time"]
		return payload["comments"], payload["poll_delay"]
		

def get_comments(fetcher):
	while True:
		comments, sleeptime = fetcher.fetch()
		for c in comments:
			print(c)
			yield c["comment"]
		time.sleep(min(sleeptime / 1000, 0.2))

#for c in get_comments():
#	print(c)
fetcher = FetchTube("3AsO2f9oxP0")
for comment in get_comments(fetcher):
	print(comment)
