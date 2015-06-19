import requests

key = 'YOUR API KEY HERE'
sandbox = 'YOUR SANDBOX URL HERE'
recipient = 'YOUR EMAIL HERE'

request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'hello@example.com',
    'to': recipient,
    'subject': 'Hello',
    'text': 'Hello from Mailgun'
})

print 'Status: {0}'.format(request.status_code)
print 'Body:   {0}'.format(request.text)
