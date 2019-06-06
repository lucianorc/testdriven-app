import unittest

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase

from sqlalchemy.exc import IntegrityError


class TestUserModel(BaseTestCase):
    def test_add_user(self):
        """ Ensure model can add a new user """
        user = User(
            username='John Doe',
            email='johndoe@email.com'
        )
        db.session.add(user)
        db.session.commit()

        self.assertTrue(user.id)
        self.assertEqual(user.username, 'John Doe')
        self.assertEqual(user.email, 'johndoe@email.com')
        self.assertTrue(user.active)

    def test_add_user_duplicate_username(self):
        """
        Ensure model can't add an user with same username
        """
        user = User(
            username='John Doe',
            email='johndoe@email.com'
        )
        db.session.add(user)
        db.session.commit()

        duplicated_user = User(
            username='John Doe',
            email='anotherdoe@email.com'
        )
        db.session.add(duplicated_user)

        self.assertRaises(IntegrityError, db.session.commit())

    def test_add_user_duplicate_username(self):
        """
        Ensure model can't add an user with same email
        """
        user = User(
            username='John Doe',
            email='johndoe@email.com'
        )
        db.session.add(user)
        db.session.commit()

        duplicated_email = User(
            username='johndoe',
            email='johndoe@email.com'
        )
        db.session.add(duplicated_email)

        self.assertRaises(IntegrityError, db.session.commit())

    def test_to_json(self):
        """ Ensure model can return JSON format User data """
        user = User(
            username='John Doe',
            email='johndoe@email.com'
        )
        db.session.add(user)
        db.session.commit()

        self.assertTrue(isinstance(user.to_json(), dict))


if __name__ == '__main__':
    unittest.main()
