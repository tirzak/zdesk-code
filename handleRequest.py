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
        print("\n")
        for (k,v) in ticketList.items():
            print("{}".format(v[1]))
    else:
        print("\n{}".format(value[1]))
        print("\nDescription:\n{} \n".format(value[2]))


def getTickets(singleton, passedURL=""):
    perpageLimit=25
    if passedURL!="":
        requestURL=passedURL
    else:
        requestURL="{}/tickets.json?page[size]={}".format(URL,perpageLimit)
    response=handleRequest(requestURL).json()
    if response['meta']['has_more']:
        singleton.setHasMore(1,response['links']['next'],response['links']['next'])
    else:
        singleton.resetValue()

    outputParser.outputParser(response,singleton,1)
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









