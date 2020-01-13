import unittest
from time import sleep
import json
from config import MonitorConfig
class TestModels(unittest.TestCase):

    def test_sqlsaver1createreport(self):
        import os
        os.system('rm /mnt/shareddata/testrun.txt')
        os.system('touch /mnt/shareddata/testrun.txt')


if __name__ == '__main__':
    unittest.main()
