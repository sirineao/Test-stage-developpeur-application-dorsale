import pytest, os, unittest, psycopg2
from app import app
from db_util import *
from unittest.mock import patch

#This class test the api routes reponse status codes
class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    #This test makes sure that the route '/top/5' reponds with a 200 ok!
    @patch('db_util.db_connection')
    def test_valid_index(self, mock_get_n):
        response = self.app.get('/top/5')
        self.assertEqual(response.status_code, 200)
    
    #This test makes sure that the route '/top/e' reponds with a 404 as a letter cannot be a parameter
    @patch('db_util.db_connection')
    def test_invalid_index(self, mock_get_n):
        response = self.app.get('/top/e')
        self.assertEqual(response.status_code, 404)

    #This test makes sure that the route '/top/101' reponds with a 404 as the parameter cannot be a number higher than 100
    @patch('db_util.db_connection')
    def test_invalid_index_2(self, mock_get_n):
        mock_get_n.return_value = None
        response = self.app.get('/top/101')
        self.assertEqual(response.status_code, 404)

    #This test checks the response body
    # @patch('db_util.db_connection')
    # def test_json(self, mock_get_n):
    #     expected_value = '[{ "score": 1.0,"url": "https://inspection.canada.ca/splash"}]'
    #     mock_get_n.return_value = None
    #     response = self.app.get('/top/1')
    #     self.assertEqual(response.json(), expected_value)

if __name__ == "__main__":
    unittest.main()

