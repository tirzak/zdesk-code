class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Ticket(metaclass=Singleton):
    
    def __init__(self):
        self._ticketList={}
        self._currPage=1
        self._morePage=0
        self._next=""
        self._prev=""
    def setTicketList(self,ticketList):
        self._ticketList=ticketList
    def getTicketList(self):
        return self._ticketList
    def setCurrPage(self,currPage):
        self._currPage=currPage
    def getCurrPage(self):
        return self._currPage
    def getHasMore(self):
        return [self._morePage,self._next,self._prev]
    def setHasMore(self,value,nextURL="",prevURL=""):
        self._morePage=value
        
        self._next=nextURL
        self._prev=prevURL
    def resetValue(self):
        self._morePage=0
    def isEmpty(self):
        return len(self._ticketList)==0
    