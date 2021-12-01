def getMonth(value):
    months = {1 : "January",
           2 : "February",
           3 : "March",
           4 : "April",
           5 : "May",
           6 : "June",
           7 : "July",
           8 : "August",
           9 : "September",
           10: "October",
           11: "November",
           12: "December"
        }
    return months[value]

def dateParser(value):
    value=value.split("T")[0].split("-")
    
    dateString = "{} {}, {}".format(getMonth(int(value[1])),value[2],value[0])
    return dateString

def outputParser(response, singleton,flag):
    if flag == 1:
        ticketList = {}
        
        for idx, val in enumerate(response['tickets']):
            ticketString = "{}) Ticket with subject '{}' opened by {} on {}".format(val['id'], val['subject'], val['requester_id'], dateParser(val['created_at']))
            ticketList[val['id']]={1: ticketString,2:val['description']}
            
        singleton.setTicketList(ticketList)
    
    else:
        val = response['ticket']
        ticketString = "{}) Ticket with subject '{}' opened by {} on {}".format(val['id'], val['subject'], val['requester_id'], dateParser(val['created_at']))
        return {1: ticketString,2:val['description']}
    