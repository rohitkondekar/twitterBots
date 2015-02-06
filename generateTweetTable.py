import os
import sys
import urllib2
import json
import graphlab as gl


tweetsURL = "http://smisc-api.jacobgreenleaf.com/tweets"
tweets = json.load(urllib2.urlopen(tweetsURL))

g = gl.SGraph()

dictTweets = dict()

for tweet in tweets:
	dictTweets.setdefault('user_id',[]).append(tweet['user_id'])
	dictTweets.setdefault('text',[]).append(tweet['text'])
	dictTweets.setdefault('created_at',[]).append(tweet['created_at'])
	dictTweets.setdefault('id_str',[]).append(tweet['id_str'])

gtable = gl.SFrame(dictTweets)
gtable.save('./tweetTable')