import requests
from requests.auth import HTTPBasicAuth
import json
import config
with open('tickets.json') as f:
  datas= json.load(f)

URL="https://zcckry.zendesk.com/api/v2/tickets.json"
URL2="https://zcckry.zendesk.com/api/v2/tickets/create_many"
base64Token="{}".format(config.email, config.password)
head = {'Authorization': 'Basic '}
print(head)
def getTickets():
    response=requests.get(url=URL, headers=head)
    print(response.json())





