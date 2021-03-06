#!/usr/bin/env python

# Code samples for blog post
# http://mikethetechie.com/post/6975966936/controlling-the-environment-cloud-control-apis
#
#Import the Openstack swift (1.3.0) module to access the Rackspace cloudfiles api.
# Download from https://launchpad.net/swift/
# Then use setup.py install.

import secrets # import user name RACKSPACE_USER and API key RACKSPACE_KEY
import swift.common.client
from pprint import pprint
from swift.common.client import  get_auth, get_account, get_container, put_object, Connection


# Open a connection to the rackspace Cloud with the user and ke.
conn = Connection('https://auth.api.rackspacecloud.com/v1.0',secrets.RACKSPACE_USER, secrets.RACKSPACE_KEY)
# Get some data about the account, including a list of storage containers.
acc = conn.get_account()
first_container_name = acc[1][0]['name']
pprint(acc)
# Redundant here, but get details of the container. 
container_object = conn.get_container(first_container_name )
pprint(container_object)
# Now create  new file within the first container and upload some text contents.
destination_name='openstacktest.txt' 
contents = "blah blah blah"
content_type = 'text/html'

# version to load a file
#contents = open('xd_city_sunrise.jpg','r')
#destination_name='xd_city_sunrise.jpg'
#content_type = 'image/jpeg'

print "Creating file in container %s" % first_container_name
etag = conn.put_object(first_container_name, destination_name, contents, content_type=content_type)
pprint("Done - etag=%s" % etag)

