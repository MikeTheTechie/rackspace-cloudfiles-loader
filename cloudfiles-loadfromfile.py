#!/usr/bin/env python


""" Load a file from disk into the rackspace cloudfiles storage.
From http://www.rackspace.com/knowledge_center/index.php/Deploying_a_Cloud_Site_with_Media_content_on_Cloud_Files

API docs are locally here file:///home/mikea/dev/python-cloudfiles/docs/index.html

"""

# Code samples for blog post
# http://mikethetechie.com/post/6975966936/controlling-the-environment-cloud-control-apis
#

import secrets # import user name RACKSPACE_USER and API key RACKSPACE_KEY

import cloudfiles
conn = cloudfiles.get_connection(secrets.RACKSPACE_USER, secrets.RACKSPACE_KEY)
cont = conn.create_container('TestCloudFilesContainer')
obj  = cont.create_object('xd_logo.jpg')
obj.content_type = 'image/jpeg'
obj.load_from_filename('xd_logo.jpg')
print "File Uploaded!"
if cont.is_public == False:
    cont.make_public()