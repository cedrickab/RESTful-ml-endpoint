# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:40:09 2023

@author: hp
"""

import unittest
from flask import request
import json

class TestClassifyEndpoint(unittest.TestCase):
    def test_classify(self):
        # Prepare test data
        data = {'pixels': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,31,0,70,135,0,0,35,23,4,5,1,3,12,5,0,0,0,0,0,0,0,0,0,0,0,2,0,9,135,128,176,226,181,193,242,217,143,125,188,155,129,115,207,74,0,0,0,0,0,0,0,0,0,1,0,0,99,142,206,230,166,184,231,222,158,146,232,164,95,167,225,46,0,0,0,0,0,0,0,0,0,1,0,0,99,180,212,154,84,106,212,172,82,86,177,189,87,146,220,6,0,0,0,0,0,0,0,0,0,1,0,0,162,229,195,58,87,108,97,94,121,141,93,79,108,85,255,0,0,0,0,0,0,0,0,0,0,4,0,171,239,221,125,96,86,102,117,68,93,75,96,89,107,77,173,0,0,0,0,0,0,0,0,0,0,0,0,8,177,177,39,131,86,89,87,95,87,73,80,89,81,97,131,0,0,0,0,0,0,0,0,0,0,0,0,0,41,115,66,100,73,136,141,80,90,74,105,97,117,133,46,0,0,0,0,0,0,0,0,0,0,2,0,27,167,74,116,41,112,137,83,122,113,99,79,107,88,133,63,0,0,0,0,0,0,0,0,0,0,6,0,70,232,168,138,98,75,114,120,120,95,98,97,92,75,154,55,0,1,1,0,0,0,0,0,0,2,1,0,0,139,183,178,173,90,107,128,80,100,103,93,103,98,123,16,0,0,0,0,0,0,0,0,0,0,0,0,0,89,190,201,215,121,93,95,102,101,111,124,113,133,151,4,0,0,0,0,0,0,0,0,0,0,0,10,30,42,95,117,194,171,173,217,179,148,144,125,138,125,126,1,0,0,0,0,0,0,1,1,0,0,29,44,45,57,73,89,101,106,119,96,111,93,138,131,124,90,125,25,0,0,0,0,0,1,0,0,6,40,41,35,64,89,98,113,124,134,142,87,144,88,99,135,121,98,122,101,0,0,0,1,0,0,2,31,52,48,53,68,79,96,115,114,115,130,131,83,108,133,154,129,116,118,115,137,0,0,0,0,0,21,50,43,46,61,69,95,116,112,112,120,125,129,117,181,152,161,136,137,134,128,102,153,13,0,0,8,47,53,45,51,63,79,93,115,132,131,123,129,129,116,110,137,129,113,118,135,138,115,99,126,0,0,25,61,53,56,66,70,104,117,122,122,113,115,110,104,106,93,86,136,84,95,88,108,114,117,115,121,10,11,89,75,71,101,117,119,129,125,125,114,99,98,114,119,120,103,102,159,134,138,113,106,95,94,87,107,24,57,100,106,103,111,122,119,107,110,113,98,89,88,85,94,87,81,73,82,78,81,79,82,88,93,101,132,24,71,68,58,66,63,57,58,61,67,69,78,89,103,111,114,123,135,139,130,135,135,131,132,134,134,119,126,19,94,139,137,136,139,138,142,146,139,149,136,136,141,135,138,135,136,128,122,124,128,120,121,119,116,103,132,31,1,57,82,45,90,69,111,61,122,50,121,40,103,32,103,34,81,47,69,80,48,123,12,110,115,102,79,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
                # Call the API endpoint
        url = "http://127.0.0.1:5000/classify"
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        result = response.json()

        # Assert that the result matches the expected value
        self.assertEqual(result["classification"], 4)

if __name__ == '__main__':
    unittest.main()

