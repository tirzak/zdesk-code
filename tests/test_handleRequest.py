import unittest
from src import handleRequest
from src import singleton
import asyncio
import io
import sys

class TestHandleRequest(unittest.TestCase):

    def testAllTicket(self):
        sg=singleton.Singleton()
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                    
        asyncio.run(handleRequest.getTickets(sg))                  
        sys.stdout = sys.__stdout__     
        self.assertFalse(sg.isEmpty())
    def testOneTicketWithCorrectTicketID(self):
        sg=singleton.Singleton()         
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                
        test=asyncio.run(handleRequest.getOneTicket(1,sg))
        sys.stdout = sys.__stdout__   
        self.assertNotEqual(len(test),0)  
    def testOneTicketWithIncorrectTicketID(self):
        sg=singleton.Singleton()         
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                
        test=asyncio.run(handleRequest.getOneTicket(-22,sg))
        sys.stdout = sys.__stdout__   
        self.assertEqual(test,None)   
    






if __name__ == "__main__":
     unittest.main()