class Singleton:
    def __init__(self) -> None:
        self._ticketList={}
        self._currPage=0
        self._totalPage=0
    def setTicketList(self,ticketList):
        self._ticketList=ticketList
    def getTicketList(self):
        return self._ticketList
    def setCurrPage(self,currPage):
        self._currPage=currPage
    def getCurrPage(self):
        return self._currPage
    def getTotalPage(self):
        return self._totalPage
    def setTotalPage(self,totalPage):
        self._totalPage=totalPage
  

    
        