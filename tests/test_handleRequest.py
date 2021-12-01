import unittest
from src import handleRequest
from src.singleton import Ticket
import asyncio
import io
import sys

class TestHandleRequest(unittest.TestCase):
    #Test with correct ticket ID. Should receive a dict with 2 values
    def testOneTicketWithCorrectTicketID(self): 
        sg=Ticket()   
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                
        test=asyncio.run(handleRequest.getOneTicket(56,sg))
        sys.stdout = sys.__stdout__   
        self.assertNotEqual(len(test),0)  

    #Test with Incorrect ticket ID. Should receive nothing
    def testOneTicketWithIncorrectTicketID(self):
        sg=Ticket()       
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                
        test=asyncio.run(handleRequest.getOneTicket(-22,sg))
        sys.stdout = sys.__stdout__   
        self.assertEqual(test,None) 
        
    #Test all ticket function. Singleton should have a non empty dict
    def testAllTicket(self):
        sg=Ticket()
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                    
        asyncio.run(handleRequest.getTickets(sg))                  
        sys.stdout = sys.__stdout__     
        self.assertFalse(sg.isEmpty())
    
    






if __name__ == "__main__":
     unittest.main()