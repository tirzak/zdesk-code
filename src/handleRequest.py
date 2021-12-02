import base64
import aiohttp
import asyncio
import time


from src.singleton import Ticket
from src import outputParser
from config import config 

#Initialize singleton class
sg=Ticket()

#For colored output
def Red(val): 
    print('\033[91m {}\033[00m' .format(val))
def Yellow(val): 
    print('\033[93m {}\033[00m' .format(val))

#Subdomain URL
URL='https://{}/api/v2'.format(config.subdomain)

#Encode user credentials in base64
base64Token='{}/token:{}'.format(config.email, config.apiToken)
base64Token_bytes = base64Token.encode('ascii') 
base64_bytes = base64.b64encode(base64Token_bytes)
base64_string = base64_bytes.decode('ascii')
head = {'Authorization': 'Basic {}'.format(base64_string)} #header


#The method fetches data for a given URL
async def fetch(session, url):
    async with session.get(url) as resp:
            data = await resp.json()
            if resp.status == 200: #If successful, return the response
                return data
            else:#Else, print error
                if resp.status==404:
                    Red('Invalid Ticket ID, Error: {}'.format(data['error']))
                elif resp.status==401:
                    Red('Authentication failed. Please check your credentials, Error: {}'.format(data['error']))
                else:
                    Red('HTTP Error: {}'.format(data))
        
       

            
#This function can print either a dict of dicts or a dict
def printTicket(ticketList, flag,value=''):
    #flag is 1, when the function is receiving a dict of dicts
    if flag == 1:
        print('\n')
        for (k,v) in ticketList.items():
            print('{} \033[93m Status: \033[00m {}'.format(v[1],v[3].title()))
    else:                               #else, print the dict values
        print('\n{}'.format(value[1]))
        Yellow('\nStatus: ')
        print(value[3])
        Yellow('\nDescription:')
        print(value[2],'\n')


#This function prints a list of 25 tickets. It is asynchronous to avoid blocking in case of multiple api calls
async def getTickets(single, passedURL=''):
    perpageLimit=25
    if passedURL!='':
        requestURL=passedURL
    else:
        requestURL='{}/tickets.json?page[size]={}'.format(URL,perpageLimit) #
    try:
        async with aiohttp.ClientSession(headers=head) as session:

                    tasks = []
                    
                    tasks.append(asyncio.ensure_future(fetch(session, requestURL)))

                    response = await asyncio.gather(*tasks)
                    response=response[0]
                    if response:
                        
                        #Set previous and next url based on the response to allow pagination
                        seconds = time.time()
                        sg.setTimeStamp(seconds)
                        if response['meta']['has_more']:
                            sg.setHasMore(1,response['links']['next'],response['links']['prev'])
                        elif not response['meta']['has_more'] and sg.getCurrPage()>1:
                            sg.setHasMore(0,prevURL=response['links']['prev'])
                       
                        parsedResp=outputParser.outputParser(response,1)
                        printTicket(sg.getTicketList(),1,parsedResp)
    except aiohttp.client_exceptions.ClientConnectorError as err:
        print ('Connection Error, ',err)
    

#This function returns and prints a single ticket.
async def getOneTicket(value, single):
    ticketL= sg.getTicketList()
    value = int(value)
    seconds = time.time()
    timeStamp = sg.getTimeStamp()
    diff = seconds-timeStamp
    #If the ticket was received in a getAllTicket() call, return it from cache.
    #If it has been more than 45 seconds, skip cache
    if value in ticketL and diff < 45:
         printTicket(ticketL,2,ticketL[value])

    else:                   #Else, make an api call
        requestURL='{}/tickets/{}.json'.format(URL,value)
        try:
            async with aiohttp.ClientSession(headers=head) as session:

                    tasks = []
                    
                    tasks.append(asyncio.ensure_future(fetch(session, requestURL)))

                    response = await asyncio.gather(*tasks)
                    response=response[0]
                    if response:
                
                        parsedResp=outputParser.outputParser(response,2)
                        printTicket(ticketL,2,parsedResp)
                        return parsedResp #return the response for tests
        except aiohttp.client_exceptions.ClientConnectorError as err:
            print ('Connection Error, ',err)
        









