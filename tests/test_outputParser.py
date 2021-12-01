import unittest
from src.singleton import Ticket
from src import outputParser
class TestHandleRequest(unittest.TestCase):

    #Test output parser with a single dict mimicking a ticket object. Should receive a dict with 2 values
    def testOutputParserWithASingleDict(self):

        x= {"ticket": {
                "created_at": "2009-07-20T22:55:29Z",
                "description": "The fire is very colorful.",
                "id": 35436,
                "priority": "high",
                "requester_id": 20978392,
                "status": "open",
                "subject": "Help, my printer is on fire!",
                "submitter_id": 76872,
                "type": "incident"
            }
            }
        result = outputParser.outputParser(x,2)
        self.assertEqual(len(result),2)

    #Test output parser with dict mimicking a list of tickets. Singleton should have a non empty dict
    def testOutputParserWithAnArray(self):
        sg=Ticket()

        x= {"tickets": [ {
                "created_at": "2009-07-20T22:55:29Z",
                "description": "The fire is very colorful.",
                "id": 35436,
                "priority": "high",
                "requester_id": 20978392,
                "status": "open",
                "subject": "Help, my printer is on fire!",
                "submitter_id": 76872,
                "type": "incident"
            }]
            }
        outputParser.outputParser(x,1)
        self.assertFalse(sg.isEmpty())
   
 
    





if __name__ == "__main__":
     unittest.main()