import urllib2, json, urllib

API_KEY = '1f366e0712bd4ad6b079afe3bb993434'
STATES = ['mo']
FIELDS = ['title','sponsors']

for state in STATES:
	response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&fields=title,sponsors').read()

bills = json.loads(response)



for bill in bills:
    # This is the processing piece I mentioned in the assignment description. To include
    # a bill ID (which has spaces in it) through a URL in Python, you need to do this first.
    encoded_bill_id = urllib.unquote(bill['sponsors'][0]['name'])
    print encoded_bill_id
    print bill['title']
    