import requests
from requests.auth import HTTPBasicAuth
import json
import base64

from requests.models import Response
import config
import outputParser


URL="https://zcckry.zendesk.com/api/v2"
base64Token="{}:{}".format(config.email, config.password)
base64Token_bytes = base64Token.encode("ascii") 
base64_bytes = base64.b64encode(base64Token_bytes)
base64_string = base64_bytes.decode("ascii")
head = {'Authorization': 'Basic {}'.format(base64_string)}


def handleRequest(requestUR):
    response=requests.get(url=requestUR, headers=head)
    return response

def printTicket(ticketList, flag,value=""):
    if flag == 1:
        for (k,v) in ticketList.items():
            print("{}".format(v))
    else:
        print("\n{}".format(value))


def getTickets(singleton):
    perpageLimit=25
    requestURL="{}/tickets.json?page[size]={}".format(URL,perpageLimit)
    response=handleRequest(requestURL)
    outputParser.outputParser(response.json(),singleton,1)
    printTicket(singleton.getTicketList(), 1)

def getOneTicket(value, singleton):
    ticketL= singleton.getTicketList()
    value = int(value)
    if value in ticketL:
        printTicket(ticketL,2,ticketL[value])
    else:
        requestURL="{}/tickets/{}.json".format(URL,value)
       
        response=handleRequest(requestURL)
        
        parsedResp=outputParser.outputParser(response.json(),singleton,2)
        printTicket(ticketL,2,parsedResp)









