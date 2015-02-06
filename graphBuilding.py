import os
import sys
import urllib2
import json
import graphlab as gl

usersURL = "http://smisc-api.jacobgreenleaf.com/user"
followersURL = "http://smisc-api.jacobgreenleaf.com/edges/near/1000000000/followers/"

users = json.load(urllib2.urlopen(usersURL))

edgeFile = "graphLibEdgeFile.txt"


g = gl.SGraph()

for user in users:
	userId = user['id_str']
	followers = json.load(urllib2.urlopen(followersURL+userId))
	for follower in followers:
		g = g.add_edges(gl.Edge(follower['from_user'],follower['to_user']))

print g
g.save("followerGraph")




