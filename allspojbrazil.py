import urllib2
import re

from gemadb import Problem

html = urllib2.urlopen("http://br.spoj.com/problems/main/").read()
main_html = re.search(r'problemas</a><br>(.*?)search', html, re.UNICODE | re.DOTALL)

categories_pattern = re.compile(r'"/problems/(.*?)"', re.UNICODE | re.DOTALL)

for category_match in categories_pattern.finditer(main_html.group(1)):
	print "%s" % category_match.group(1)
	page_url = "/problems/%s/" % category_match.group(1)
	page_html = urllib2.urlopen("http://br.spoj.com" + str(page_url)).read()
	
	while(1):
		#LOAD PROBLEMS
		REGEX = r'<a href="/problems/(.*?)/.*?<b>(.*?)<.*?ranks.*?>(\d+).*?status.*?>(.*?)<'
		pattern = re.compile(REGEX, re.UNICODE | re.DOTALL)
		for match in pattern.finditer(page_html):
			data = {
				'name': "%s" % unicode(match.group(2), "ISO-8859-1"),
				'jid': "%s" % match.group(1),
				'judge_id':'2', #id on gemadb
				'url': "http://br.spoj.com/problems/%s/" % match.group(1),
				'total_users': "%s" % match.group(3),
				'accepted_users': "%d" % int(float(match.group(4))*int(match.group(3))/100),
				'total_submissions':-1,
				'accepted_submissions':-1,
				'description':'',
				'spoiler':'',
				'tag_ids':[]
			}
			p = Problem(data)
			print p			
			#if p.save():
			#	print "Problem %s saved " % data['jid']
			#else:
			#	print "Problem %s NOT saved " % data['jid']
			break
		more_page_html = re.search(r'<a href="' + re.escape(str(page_url)) + r'sort=(\d+),start=(\d+)" class="pager_link">Pr', 
						page_html, re.UNICODE | re.DOTALL)
		if more_page_html:
			new_url = "sort=%s,start=%s" % (more_page_html.group(1), more_page_html.group(2))
			page_html = urllib2.urlopen("http://br.spoj.com" + str(page_url) + str(new_url)).read()
		else:
			break
	break
