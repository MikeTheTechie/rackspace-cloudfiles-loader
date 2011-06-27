#!/usr/bin/env python
#Import the CloudFiles Python API ensure this is located in your lib directory for Python.

# Code samples for blog post
# http://mikethetechie.com/post/6975966936/controlling-the-environment-cloud-control-apis
#

import secrets # import user name RACKSPACE_USER and API key RACKSPACE_KEY

import cloudfiles
#Lets Connect to CloudFiles.
conn = cloudfiles.get_connection(secrets.RACKSPACE_USER, secrets.RACKSPACE_KEY)
#Creating a Container Object.
cont = conn.create_container('TestCloudFilesContainer')
#Now for the Object.
obj  = cont.create_object('index2.html')
obj.content_type = 'text/html'

#Finally for some data.
obj.write('<html><head></head><body><img src="xd_logo.jpg"><br />Hello world!</body></html>')
print "Done!"