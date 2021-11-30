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
        elif int(menuAnswer) ==1:
            hR.getTickets(sg)
            print("Page {} of {}. Type 'n' to go to the next page".format(sg.getCurrPage(),sg.getTotalPage()))
        elif int(menuAnswer )==2:
            ticketValue=input("Please enter a ticket number: ")
            hR.getOneTicket(ticketValue,sg)
        print(menuValues)
        menuAnswer=input()
    print("Quitting. Thanks for using the Ticket Viewer")


def main():

    welcomeMessage="""
    Welcome to the Ticket Viewer
    Type 'menu' to view the option or 'quit' to close the application
    """
    print(welcomeMessage)

    
    menuOptions()
   




if __name__ == "__main__":
    main()







