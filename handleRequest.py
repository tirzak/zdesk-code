import requests
from requests.auth import HTTPBasicAuth
import json
import base64
import config
import outputParser


URL="https://zcckry.zendesk.com/api/v2/tickets.json"
base64Token="{}:{}".format(config.email, config.password)
base64Token_bytes = base64Token.encode("ascii") 
base64_bytes = base64.b64encode(base64Token_bytes)
base64_string = base64_bytes.decode("ascii")
head = {'Authorization': 'Basic {}'.format(base64_string)}

def getTickets():
    perpageLimit=1
    response=requests.get(url="{}?per_page={}".format(URL,perpageLimit), headers=head)
    outputParser.outputParser(response.json())






