
import unittest
from src.singleton import Ticket


class TestHandleRequest(unittest.TestCase):
    #Test two singleton objects. Since singleton can have only one initialization, the two objects should be equal
    def testSingletonWithTwoObject(self):
        firstObject=Ticket()
        secondObject=Ticket()

        self.assertEqual(firstObject,secondObject)


if __name__ == "__main__":
     unittest.main()