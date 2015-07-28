import os
import unittest

from project import app, db, bcrypt
from project.config import basedir
from project.models import User

TEST_DB = 'sano-test.db'


class AllTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()
        self.assertEquals(app.debug, False)

    # executed after to each test
    def tearDown(self):
        db.drop_all()


    ########################
    #### helper methods ####
    ########################

    def login(self, name, password):
        return self.app.post('/', data=dict(
            name=name, password=password), follow_redirects=True)

    def register(self, name, email, password, confirm):
        return self.app.post(
            'register/',
            data=dict(name=name, email=email, password=password, confirm=confirm),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get('logout/', follow_redirects=True)

    def create_user(self, name, email, password):
        new_user = User(
            name=name,
            email=email,
            password=bcrypt.generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

    def create_admin_user(self):
        new_user = User(
            name='Superman',
            email='admin@realpython.com',
            password=bcrypt.generate_password_hash('allpowerful'),
            role='admin'
        )
        db.session.add(new_user)
        db.session.commit()


    ###############
    #### tests ####
    ###############

    def test_users_can_register(self):
        new_user = User("michael", "michael@mherman.org", "michaelherman")
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == "michael"

    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please sign in to access your \\\
                      task list', response.data)
