class Singleton:
    def __init__(self) -> None:
        self._ticketList={}
        self._currPage=0
        self._totalPage=0
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
        return [self._totalPage,self._next,self._prev]
    def setHasMore(self,value,nextURL="",prevURL=""):
        self._totalPage=value
        if value==1:
            self._next=nextURL
            self._prevURL=prevURL
    def resetValue(self):
        self._totalPage=0
    def isEmpty(self):
        return len(self._ticketList)==0

    
        