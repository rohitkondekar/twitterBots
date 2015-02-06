import os
import sys
import urllib2
import json
import graphlab as gl

print sys.exec_prefix
gtable = gl.load_sframe('tweetTable')
# gtable.show()

tweets = gl.text_analytics.count_words(gtable['text'])
# tweets = tweets.dict_trim_by_keys(gl.text_analytics.stopwords(), exclude=True)

model = gl.topic_model.create(tweets,num_topics=10,num_iterations=30)

print(tweets[:2])
print(len(model['vocabulary']))
print(model.predict(tweets))


input("Press Enter to continue...")