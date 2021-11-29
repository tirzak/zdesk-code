import handleRequest as hR


def menuOptions():
    menuValues="""
    Select View Options:
        a) Type 1 to view all tickets
        b) Type 2 to view a ticket
        c) Type 'quit' to exit
    """

    print(menuValues)

    menuAnswer=input()
    if int(menuAnswer) ==1:
        hR.getTickets()


def main():
    welcomeMessage="""
    Welcome to the Ticket Viewer
    Type 'menu' to view the option or 'quit' to close the application
    """
    print(welcomeMessage)

 
    menuOptions()
   




if __name__ == "__main__":
    main()







