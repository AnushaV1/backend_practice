from unittest import TestCase

from app import app
from models import db, User


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///noyo_test_db'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    """Tests for views about desserts."""

    def setUp(self):
        """Make demo data."""

        User.query.delete()
        db.session.commit()

        user = User(firstname='test_fname',middlename='test_mname',lastname='test_lname',email='test@email.com',age=26,version_id=1)
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up fouled transactions."""

        db.session.rollback()

    def test_all_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            self.assertEqual(resp.status_code, 200)

            self.assertEqual(
                resp.json,
                {'users': [{
                    'id': self.user_id,
                    'firstname': 'test_fname',
                    'middlename': 'test_mname',
                    'lastname': 'test_lname',
                    'email': 'test@email.com',
                    'age': 26,
                    'version_id': 1

                }]})

    
    def test_create_user(self):
        with app.test_client() as client:
            resp = client.post(
                "/user", json={
                    "firstname": 'test_fname1',
                    'middlename': 'test_mname1',
                    'lastname': 'test_lname1',
                    'email': 'test1@email.com',
                    'age': 30,
                    'version_id': 1
                })
            self.assertEqual(resp.status_code, 201)

        
            self.assertIsInstance(resp.json['user']['id'], int)
            self.user_id = int(resp.json['user']['id'])
            

            self.assertEqual(
                resp.json,
                {"user": {
                    "id": self.user_id,
                    "firstname": 'test_fname1',
                    "middlename": 'test_mname1',
                    "lastname": 'test_lname1',
                    "email": 'test1@email.com',
                    "age": 30,
                    "version_id": 1
                }
                })

            self.assertEqual(User.query.count(), 2)

    def test_update_user(self):
        with app.test_client() as client:
            url = f"/user/{self.user_id}"
            resp = client.patch(url, json={
                "firstname": "TestName",
                "middlename": "TestMiddle",
                "age": 37               
})

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(User.query.count(), 1)
    
    def test_update_user_missing(self):
        with app.test_client() as client:
            url = f"/user/8899999"
            resp = client.patch(url, json={
                "firstname": "TestName1",
                "middlename": "TestMiddle1",
                "age":40               
})

            self.assertEqual(resp.status_code, 404)
 
    def test_delete_user(self):
        with app.test_client() as client:
            url = f"/user/{self.user_id}"
            resp = client.delete(url)

            self.assertEqual(resp.status_code, 200)

            data = resp.json
            self.assertEqual(data, {"message": "deleted"})

            self.assertEqual(User.query.count(), 0)

    def test_delete_user_missing(self):
        with app.test_client() as client:
            url = f"/user/999999"
            resp = client.delete(url)

            self.assertEqual(resp.status_code, 404)
