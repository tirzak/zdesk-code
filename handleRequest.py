import requests
import base64

from requests.models import Response
import config
import outputParser
def Red(val): 
    print("\033[91m {}\033[00m" .format(val))
def Yellow(val): 
    print("\033[93m {}\033[00m" .format(val))

URL="https://zcckry.zendesk.com/api/v2"
base64Token="{}:{}".format(config.email, config.password)
base64Token_bytes = base64Token.encode("ascii") 
base64_bytes = base64.b64encode(base64Token_bytes)
base64_string = base64_bytes.decode("ascii")
head = {'Authorization': 'Basic {}'.format(base64_string)}
code="\x1B["

def handleRequest(requestUR):
    try:
        response=requests.get(url=requestUR, headers=head)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        print("Connection Timed Out. Please try again")
    except requests.exceptions.HTTPError as errh:
        if(response.status_code==404):
            Red("Invalid Ticket ID, {}".format(errh))
        elif(response.status_code==401):
            Red("Authentication failed. Please check your credentials, {}".format(errh))
        else:
            Red("HTTP Error: {}".format(errh))
        
    except requests.exceptions.RequestException as e:
        Red("It is not you. It is us. Please restart the application")
        raise SystemExit(e)

def printTicket(ticketList, flag,value=""):
    if flag == 1:
        print("\n")
        for (k,v) in ticketList.items():
            print("{}".format(v[1]))
    else:
        print("\n{}".format(value[1]))
        Yellow("\nDescription:\n{} \n".format(value[2]))


def getTickets(singleton, passedURL=""):
    perpageLimit=25
    if passedURL!="":
        requestURL=passedURL
    else:
        requestURL="{}/tickets.json?page[size]={}".format(URL,perpageLimit)
    response=handleRequest(requestURL)
    if response:
        response=response.json()
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
        if response:
            response=response.json()
            
            parsedResp=outputParser.outputParser(response,singleton,2)
            printTicket(ticketL,2,parsedResp)









