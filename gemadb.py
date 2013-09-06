import json
import urllib2

class Problem:
    def __init__(self, data):
        self.problems_url = "http://gemadb-rrp.rhcloud.com/problems"
        self.data = data

    def __str__(self):
        return ', '.join("%s=%r" % (key,val) for (key,val) in self.data.iteritems())

    def save(self):
        json_data = json.dumps(self.data)
        length    = len(json_data)
        req = urllib2.Request(problems_url, json_data,
            {'Content-Type': 'application/json', 'Content-Length': length})
        f = urllib2.urlopen(req)
        status = f.getcode()
        f.close()

        return status == 200

#Example
if __name__ == "__main__":
    data = {
        'name':'test',
        'url':'http://example.com',
        'jid':'1234',
        'total_submissions':-1,
        'accepted_submissions':-1,
        'total_users':-1,
        'accepted_users':-1,
        'description':'',
        'spoiler':'',
        'judge_id':'',
        'tag_ids':[]
    }
    p = Problem(data)
    if p.save():
        print "SUCCESS!"
    else:
        print "FAIL!"
