import handleRequest as hR
import singleton
sg = singleton.Singleton()
def menuOptions():
    menuValues="""
    Select View Options:
        a) Type 1 to view all tickets
        b) Type 2 to view a ticket
        c) Type 'quit' to exit
    """
    menuAnswer=input()
    

    while menuAnswer != "quit":
        if menuAnswer == "menu":
            print(menuValues)
            menuAnswer=input()
            continue
        elif menuAnswer =="1":
            hR.getTickets(sg)
            obj=sg.getHasMore()
            if obj[0]==1:
                print("Only showing 25 results. Type 'n' to go to the next page. Or,")

        elif menuAnswer=="2":
            ticketValue=input("Please enter a ticket number: ")
            hR.getOneTicket(ticketValue,sg)
        elif menuAnswer=="n" and obj[0]==1:
            hR.getTickets(sg,obj[1])
            obj=sg.getHasMore()
            if obj[0]==1:
                print("Only showing 25 results. Type 'n' to go to the next page. Or,")

        menuAnswer=input("Type 'menu' to view the options or 'quit' to close the application: ")
        
    print("Quitting. Thanks for using the Ticket Viewer")


def main():

    welcomeMessage="""
    Welcome to the Ticket Viewer
    Type 'menu' to view the options or 'quit' to close the application
    """
    print(welcomeMessage)

    
    menuOptions()
   




if __name__ == "__main__":
    main()







