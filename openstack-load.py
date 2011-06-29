#!/usr/bin/env python

# Load files to Rackspace cloud or potentially other openstack "Swift" (storage) compatible cloud providers.
# @MikeTheTechie, June 2011.
#
# based on the Code samples for blog post
# http://mikethetechie.com/post/6975966936/controlling-the-environment-cloud-control-apis
#
#Import the Openstack swift (1.3.0) module to access the Rackspace cloudfiles api.
# Download from https://launchpad.net/swift/
# Then use setup.py install.

import secrets # import user name RACKSPACE_USER and API key RACKSPACE_KEY
import swift.common.client
from pprint import pprint
from swift.common.client import  get_auth, get_account, get_container, put_object, Connection

import argparse
import os

# Parse any command line arguments. Currently just --debug flag
parser = argparse.ArgumentParser(description='Load files to Rackspace cloud or potentially other openstack "Swift" (storage) compatible cloud providers.')
parser.add_argument('-debug','--debug',action="store_true", help='true for noisy helpful execution, false or omitted for quiet.')
parser.add_argument('-container','--container', action="store", dest="container", help='Container name at Rackspace cloudfiles')
parser.add_argument('-files','--files', action="store", dest="file_pattern", help='File name or pattern, e.g. logo.jpg or *.jpg')
parser.add_argument('-content_type','--content_type', action="store", help='content-type which will be applied to all the files on the CDN, e.g. image/jpeg, text/html')
args = parser.parse_args()
debug_mode = (args.debug)

print 'Loading files which match pattern%s to container %s with content_type=%s' % (args.file_pattern, args.container, args.content_type)

import glob
    
    
# Open a connection to the rackspace Cloud with the user and ke.
conn = Connection('https://auth.api.rackspacecloud.com/v1.0',secrets.RACKSPACE_USER, secrets.RACKSPACE_KEY)
# Get some data about the account, including a list of storage containers.
acc = conn.get_account()
#first_container_name = acc[1][0]['name']
#pprint(acc)
# Redundant here, but get details of the container. 
#container_object = conn.get_container(first_container_name )
#pprint(container_object)
# Now create  new file within the first container and upload some text contents.

# version which uploads a piece of text.

#destination_name='openstacktest.txt' 
#contents = "blah blah blah"
#content_type = 'text/html'

# initialise counters
files_processed=0
files_ok = 0

# now scan the supplied directory/pattern/file and process all the files. 
for filename in glob.glob(args.file_pattern):
    # version which uploads a file.
    if debug_mode:
        print "Creating file %s in container %s" % (filename, args.container)
    files_processed += 1
    contents = open(filename,'r')
    destination_name = os.path.split(filename)[1]
    
    try:
        etag = conn.put_object(args.container, destination_name, contents, content_type=args.content_type)
        if debug_mode:
            pprint("Done - etag=%s" % etag)
        files_ok += 1
    except Exception as ex:
        if debug_mode:
            print "Failed: Exception=%s" % (ex)

if files_processed > 0:
    print "%i files ok out of total %i processed " % (files_ok, files_processed)
else:
    print "No files."    
if files_ok < files_processed:
    print "%i errors." % (files_processed-files_ok)    
