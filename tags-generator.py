#!/usr/bin/env python

'''
tags-generator.py

Author: Julien Siwek
Based on : https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py

This script creates tags page for the site depending on the tags specified in _posts/
No plugins required.
'''

import glob
import os
from slugify import slugify
import sys
reload(sys)
sys.setdefaultencoding('Cp1252')

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*md')
total_tags = []
for filename in filenames:
    f = open(filename, 'r')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if not current_tags:
                break
            if current_tags[0] == '-':
                total_tags.extend(current_tags[1:])
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    slug = slugify(tag)
    tag_filename = tag_dir + slug + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tag-archive\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
