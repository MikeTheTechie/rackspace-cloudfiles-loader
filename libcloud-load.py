#!/usr/bin/env python
# Code samples for blog post
# http://mikethetechie.com/post/6975966936/controlling-the-environment-cloud-control-apis
#
# Note - I couldn't get this to work. For more info, see http://mikethetechie.com/private/6969971577/tumblr_lng0mzd5bg1qf6p57
import secrets # import user name RACKSPACE_USER and API key RACKSPACE_KEY

from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver
from pprint import pprint




Driver = get_driver(Provider.CLOUDFILES_UK)
conn2 = Driver(secrets.RACKSPACE_USER, secrets.RACKSPACE_KEY, 'https://lon.auth.api.rackspacecloud.com/v1.0')


containers = conn2.list_containers()
container_objects = conn2.list_container_objects(containers[0])

pprint(containers)
pprint(container_objects)


cont = conn2.create_container('Testlibcloudcontainer')
obj = cont.create_object('t.html')
obj.content_type = 'text/html'

#Finally for some data.
obj.write('<html><head></head><body><img src="xd_logo.jpg"><br />Hello world!</body></html>')


