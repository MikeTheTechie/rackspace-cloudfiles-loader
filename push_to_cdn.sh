# Loads files from local folders to the Rackspace cloudfiles storage, which is usually published as a CDN.
# Useful for copying all the static files from your website to the Rackspace cloudfiles CDN.
# This file needs to be executable, e.g. chmod 0700 push_to_cdn.sh
# Use with git@github.com:MikeTheTechie/rackspace-cloudfiles-loader.git
# @MikeTheTechie, June 2011.

python openstack-load.py --container myco-img --files "static/img/*.jpg" --content_type image/jpeg
python openstack-load.py --container myco-img --files "static/img/*.png" --content_type image/png
python openstack-load.py --container myco-img --files "static/img/*.gif" --content_type image/gif
