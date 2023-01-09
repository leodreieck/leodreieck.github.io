# adapted from https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py via http://longqian.me/2017/02/09/github-jekyll-tag/
# collects all tags used and creates a separate tagpage, if it does not exist yet.

import glob
import re

POST_DIR = '_posts/'
TAG_DIR = 'tag/'

filenames = glob.glob(POST_DIR + '*md')

# collect all used tags
total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            current_line = line.strip().split(':') 
            if current_line[0] == 'tags':
                #print(current_line)
                post_tags = current_line[1].strip().split(" ")
                #print(post_tags)
                for tag in post_tags:
                    total_tags.append(tag)
                crawl = False
                break
        # if beginning '---': set crawl to True
        # if ending '---': reset crawl to False
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()

#print(total_tags)

# get already existing tagpages
old_tags_raw = glob.glob(TAG_DIR + '*.md')
#print(old_tags_raw)
old_tags = list()
for path in old_tags_raw:
    old_tags.append(re.findall("tag\\\\(.*?).md", path)[0])
#print(old_tags)

# make sure to only create pages for new tags as old ones might have personalized description
new_tag_pages = set(total_tags) - set(old_tags)
print(new_tag_pages)

# create pages
for tag in new_tag_pages:
    tag_filename = TAG_DIR + tag.replace(' ', '_') + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\n---\n'
    f.write(write_str)
    f.close()
print("Tagpages generated for {}, count: {}".format(new_tag_pages, new_tag_pages.__len__()))
