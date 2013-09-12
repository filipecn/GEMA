import urllib2
import re
from gemadb import Tag

tags = set()

for i in range(16):

	html = urllib2.urlopen("http://codeforces.com/problemset/page/%s" % str(i+1)).read()

	tags_pattern = re.compile(r'tags/(.*?)"', re.UNICODE | re.DOTALL)

	for tag_match in tags_pattern.finditer(html):
		tags.add(tag_match.group(1))
	print "page %s" % i

print len(tags)	

tagslist = list(tags)

tagslist.sort()

for tag in tagslist[1:]:
	data = {
		'name': "%s" % tag
	}
	t = Tag(data)
	print t
#	if t.save():
#		print "Tag %s saved " % data['name']
#	else:
#		print "Tag %s NOT saved " % data['name']



