import unittest
import os

from project import app
from project.database import Base, engine, session

# Configure our app to use the testing databse
os.environ["CONFIG_PATH"] = "project.config.TestingConfig"


class AllTests(unittest.TestCase):

    def setUp(self):
        """ Test setup """
        self.client = app.test_client()

        # Set up the tables in the database
        Base.metadata.create_all(engine)

    def tearDown(self):
        """ Test teardown """
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)

    ###############
    #### tests ####
    ###############

    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please sign in to access your grocery list',
                      response.data)

if __name__ == "__main__":
    unittest.main()
