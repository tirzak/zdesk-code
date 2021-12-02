from src import handleRequest as hR
from src.singleton import Ticket
import asyncio

#Initialize a singleton class
sg = Ticket()
def Red(val): 
    print('\033[91m {}\033[00m' .format(val))
def Cyan(val): 
    print('\033[96m {}\033[00m' .format(val))
def Green(val): 
    print('\033[92m {}\033[00m' .format(val))
inView=False
#This function prints a message based on the parameter
def messages(parameter):
    if parameter == 1:
        Green("Page {}, only showing 25 results. Type 'n' to go to the next page. Or,".format(sg.getCurrPage()))
    elif parameter == 2:
         Green("Page {}, only showing 25 results. Type 'n' to go to the next page, or 'p' to go to the previous page. Or,".format(sg.getCurrPage()))
    elif parameter == 3:
         Green("Page {}, Type 'p' to go to the previous page. Or,".format(sg.getCurrPage()))

#This function handles the output message logic 
def handleOutput():
    obj=sg.getHasMore()
    if obj[0]==1 and sg.getCurrPage()==1:
        messages(1)

    elif obj[0]==0 and obj[2]!='':
        messages(3)
    else:
        messages(2)



def menuOptions():
    menuValues='''
    Select View Options:
        a) Type 1 to view all tickets
        b) Type 2 to view a ticket
        c) Type 'quit' to exit
    '''
    menuAnswer=input(' ')
    

    while menuAnswer != 'quit':
        obj=sg.getHasMore()
        if menuAnswer == 'menu':
            print(menuValues)
            menuAnswer=input(" ")
            continue
        elif menuAnswer =='1':
            sg.setCurrPage(1)
            asyncio.run(hR.getTickets(sg)) #async call to getTicket
            inView=True
            handleOutput()
           


        elif menuAnswer=='2':
            if inView is True:
                inView=False
            Cyan('Please enter a ticket number:')
            ticketValue=input(' ')
                
            if ticketValue.isnumeric():
                asyncio.run(hR.getOneTicket(ticketValue,sg))
            else:
                Red('Incorrect Input')
            
        elif menuAnswer=='n' and obj[0]==1 and inView==True: #allow going to the next page only if there is  more
            asyncio.run(hR.getTickets(sg,obj[1]))
            sg.setCurrPage(sg.getCurrPage()+1)
            handleOutput()

        elif menuAnswer=='p' and obj[2]!='' and sg.getCurrPage()!=1 and inView==True: #allow going back only if you have a previous page
         
            asyncio.run(hR.getTickets(sg,obj[2]))
             
            sg.setCurrPage(sg.getCurrPage()-1)
            handleOutput()

        else:
            Red('Sorry! Could not understand the input')

        Cyan("Type 'menu' to view the options or 'quit' to close the application: ")
        menuAnswer=input(' ')
        
    print('Quitting. Thanks for using the Ticket Viewer')


def main():

    welcomeMessage='''
    Welcome to the Ticket Viewer
    Type 'menu' to view the options or 'quit' to close the application
    '''
    Cyan(welcomeMessage)

    
    menuOptions()
   




if __name__ == '__main__':
    main()







