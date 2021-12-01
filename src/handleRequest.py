import base64
import aiohttp
import asyncio

from src.singleton import Ticket
from src import outputParser
from config import config 
sg=Ticket()
def Red(val): 
    print('\033[91m {}\033[00m' .format(val))
def Yellow(val): 
    print('\033[93m {}\033[00m' .format(val))

URL='https://{}/api/v2'.format(config.subdomain)
base64Token='{}:{}'.format(config.email, config.password)
base64Token_bytes = base64Token.encode('ascii') 
base64_bytes = base64.b64encode(base64Token_bytes)
base64_string = base64_bytes.decode('ascii')
head = {'Authorization': 'Basic {}'.format(base64_string)}
code='\x1B['


async def fetch(session, url):
    async with session.get(url) as resp:
            data = await resp.json()
            if resp.status == 200:
                return data
            else:
                if resp.status==404:
                    Red('Invalid Ticket ID, Error: {}'.format(data['error']))
                elif resp.status==401:
                    Red('Authentication failed. Please check your credentials, Error: {}'.format(data['error']))
                else:
                    Red('HTTP Error: {}'.format(data))
        
       

            

def printTicket(ticketList, flag,value=''):
    if flag == 1:
        print('\n')
        for (k,v) in ticketList.items():
            print('{}'.format(v[1]))
    else:
        print('\n{}'.format(value[1]))
        Yellow('\nDescription:')
        print(value[2],'\n')


async def getTickets(single, passedURL=''):
    perpageLimit=25
    if passedURL!='':
        requestURL=passedURL
    else:
        requestURL='{}/tickets.json?page[size]={}'.format(URL,perpageLimit)
    try:
        async with aiohttp.ClientSession(headers=head) as session:

                    tasks = []
                    
                    tasks.append(asyncio.ensure_future(fetch(session, requestURL)))

                    response = await asyncio.gather(*tasks)
                    response=response[0]
                    if response:
                        

                        if response['meta']['has_more']:
                            sg.setHasMore(1,response['links']['next'],response['links']['prev'])
                        elif not response['meta']['has_more'] and sg.getCurrPage()>1:
                            sg.setHasMore(0,prevURL=response['links']['prev'])
                        # else:
                        #     sg.resetValue()
                        parsedResp=outputParser.outputParser(response,1)
                        printTicket(sg.getTicketList(),1,parsedResp)
    except aiohttp.client_exceptions.ClientConnectorError as err:
        print ('Connection Error, ',err)
    

async def getOneTicket(value, single):
    ticketL= sg.getTicketList()
    value = int(value)
    if value in ticketL:
         printTicket(ticketL,2,ticketL[value])
    else:
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
                        return parsedResp
        except aiohttp.client_exceptions.ClientConnectorError as err:
            print ('Connection Error, ',err)
        









