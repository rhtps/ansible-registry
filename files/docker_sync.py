#!/usr/bin/env python

from __future__ import print_function
from urllib2 import urlopen
import json
from docker import Client

query_url = 'https://registry.access.redhat.com/v1/search?q=*'
tags_url = 'https://registry.access.redhat.com/v1/repositories/IMAGE/tags'

cli = Client(base_url='unix://var/run/docker.sock', version='1.21')

all_images = json.loads(str(urlopen(query_url).read()))
for image in all_images['results']:
    image_name = image['name']
    if image_name.startswith('openshift') or image_name.startswith('rhel') or image_name.startswith('jboss') or image_name.startswith('rhscl'):
        if 'beta' not in image_name:
            # print(image_name + ' ', end='')
            image_tags_url = tags_url.replace('IMAGE', image_name)
            image_tags = json.loads(str(urlopen(image_tags_url).read()))
            if image_tags.get('latest'):
                latest_id = image_tags['latest']
            else:
                if 'rhel6.9' in image_name:
                    latest_id = '83dd6c1a43c7793f5e37d901019716c603e8211e962b4c762fa9f99382e0635e'
                else:
                    print("don't know what to do with " + image_name)
                    continue
            all_tags = ['latest']
            for key in image_tags.keys():
                if image_tags[key] == latest_id:
                    all_tags.append(key)
            for tag in all_tags:
                # print(tag + ' ', end='')
                cli.pull('registry.access.redhat.com/' + image_name, tag)
                # The push isn't working. For some reason latest_id doesn't jive
                # with what I'm expecting it to be. For now we'll use the older
                # docker_load.sh method.
                # cli.tag(image_name, 'localhost:5000', tag)
                # cli.push('localhost:5000', image_name, tag, insecure_registry=True)
            # print('\n', end='')

