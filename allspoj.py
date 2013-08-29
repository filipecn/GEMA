import urllib2
import re

from gemadb import Problem

html = urllib2.urlopen("http://www.spoj.com/problems/").read()
main_html = re.search(r'problems</a><br>(.*?)search', html, re.UNICODE | re.DOTALL)

categories_pattern = re.compile(r'"/problems/(.*?)"', re.UNICODE | re.DOTALL)

for category_match in categories_pattern.finditer(main_html.group(1)):
	print "%s" % category_match.group(1)
	page_url = "/problems/%s/" % category_match.group(1)
	page_html = urllib2.urlopen("http://www.spoj.com" + str(page_url)).read()
	
	while(1):
		#LOAD PROBLEMS
		REGEX = r'problemrow.*?<a href="/problems/(.*?)/.*?<b>(.*?)<.*?ranks.*?>(\d+).*?status.*?>(.*?)<'
		pattern = re.compile(REGEX, re.UNICODE | re.DOTALL)
		for match in pattern.finditer(page_html):
			p = Problem()
			p.judge = "spoj"
			p.judge_id = "%s" % match.group(1)
			p.name = "%s" % match.group(2)
			p.url = "http://www.spoj.com/problems/%s/" % match.group(1)
			p.users = "%s" % match.group(3)
			p.accepted = "%s" % match.group(4)
			p.dump()
		
		more_page_html = re.search(r'<a href="' + re.escape(str(page_url)) + r'sort=(\d+),start=(\d+)" class="pager_link">Ne', 
						page_html, re.UNICODE | re.DOTALL)
		if more_page_html:
			new_url = "sort=%s,start=%s" % (more_page_html.group(1), more_page_html.group(2))
			page_html = urllib2.urlopen("http://www.spoj.com" + str(page_url) + str(new_url)).read()
		else:
			break
