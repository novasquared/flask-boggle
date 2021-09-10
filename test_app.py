import json

from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<form id="newWordForm">', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            resp = client.post("/api/new-game")
            print(f"resp = {resp}")
            resp_dict = json.loads(resp.data)
            # print(resp_dict)
            # html = resp.get_data(as_text=True)
        
            self.assertIsInstance(resp_dict, dict)
            self.assertIsInstance(resp_dict["gameId"], str)
            self.assertIsInstance(resp_dict["board"], list)

            for item in resp_dict["board"]:
                self.assertIsInstance(item, list)
            # write a test for this route

# try:
#     json_object = json.loads(ini_string)
#     print ("Is valid json? true")
# except ValueError as e:
#     print ("Is valid json? false")