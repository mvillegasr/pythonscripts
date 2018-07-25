#! python3
# earthWallpapers.py - Downloads all pictures on the front page of /r/earthporn.

import praw, os, requests

from creds import *

reddit = praw.Reddit(user_agent=myUserAgent,
                     client_id=myClientId, 
                     client_secret=myClientSecret)

os.makedirs('C:/MyPythonScripts/earthwallpapers', exist_ok=True)

subreddit = reddit.subreddit('earthporn')

for submission in subreddit.hot(limit=25):
	image_url = '' + submission.url
	exists = os.path.isfile("/MyPythonScripts/earthwallpapers/{0}".format(os.path.basename(image_url)))
	if exists == False:
		print('Downloading image ', submission.url, '...')
		r = requests.get(image_url, stream=True)
		#TODO: check if image is in an imgur album
		with open(os.path.join(os.sep, 'MyPythonScripts', 'earthwallpapers', os.path.basename(image_url)), 'wb') as jpg:
			for chunk in r.iter_content(chunk_size=1024):
				if chunk:
					jpg.write(chunk)
	else:
		print("Image already exists")
print('Done.')
input('Press ENTER to exit')


