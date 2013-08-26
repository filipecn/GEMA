import urllib2
import re

#PROBLEM SET VOLUMES

url =  "http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=1"
response = urllib2.urlopen(url)
html = response.read()

REGEX = r'<td><a href="(.*)">Volume'
pattern = re.compile(REGEX, re.UNICODE)

for match in pattern.finditer(html):
	print "%s" % (match.group(1))
	problems_html = urllib2.urlopen("http://uva.onlinejudge.org/%s" % (match.group(1))).read()

	PROBLEM_REGEX = 'page=show_problem&amp'#;problem=(\d+)">(\d+)&nbsp;-&nbsp;(.*)</a></td>'
	problem_pattern = re.compile(PROBLEM_REGEX, re.UNICODE)
	print problems_html
	for problem_match in problem_pattern.finditer(problems_html):
		print "%s %s %s" % (problem_match.group(1), problem_match.group(2), problem_match.group(3))
#						<td align="right">548754</td>
#			<td>
#			
#
#			
#	<div style="width:150px;height:15px;background-color:#ff0000;position:relative;">
#	<div style="width:27.31%;height:100%;background-color:#00ff00;"></div>
#	<div style="width:100%;height:100%;text-align:center;position:absolute;top:-2px;left:0;font-size:13;font-family:Tahoma,Verdana,Arial,sans-serif;">27.31%</div>
#	</div>
#
#
#			
#			</td>
#
#
#									<td align="right">78437</td>
#			<td>
#	<div style="width:150px;height:15px;background-color:#ff0000;position:relative;">
#	<div style="width:72.66%;height:100%;background-color:#00ff00;"></div>
#	<div style="width:100%;height:100%;text-align:center;position:absolute;top:-2px;left:0;font-size:13;font-family:Tahoma,Verdana,Arial,sans-serif;">72.66%</div>
#	</div>
