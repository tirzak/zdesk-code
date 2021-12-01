import unittest
from src import singleton
from src import outputParser
class TestHandleRequest(unittest.TestCase):

    def testOutputParserWithASingleDict(self):
        sg=singleton.Singleton()

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
        result = outputParser.outputParser(x,sg,2)
        self.assertEqual(len(result),2)

    def testOutputParserWithAnArray(self):
        sg=singleton.Singleton()

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
        outputParser.outputParser(x,sg,1)
        self.assertFalse(sg.isEmpty())
   
 
    





if __name__ == "__main__":
     unittest.main()