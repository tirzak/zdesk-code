import requests
from requests.auth import HTTPBasicAuth
import json
with open('tickets.json') as f:
  datas= json.load(f)

URL="https://zcckry.zendesk.com/api/v2/tickets.json"
URL2="https://zcckry.zendesk.com/api/v2/tickets/create_many"
URL3="https://zcckry.zendesk.com/api/v2/job_statuses/82772a89b28a97ae57efbbdd8fd45dfc.json"
head = {'Authorization': 'Basic email_address/token:api_token {}'.format()}
def getTickets():
    response=requests.get(url=URL3, auth=HTTPBasicAuth('', ''))
    print(response.json())



